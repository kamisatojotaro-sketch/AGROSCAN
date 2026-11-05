"""
AgroScan — MobileNetV2 Transfer Learning Training Script
Dataset: PlantVillage (Kaggle)

Usage:
  1. Download dataset: https://www.kaggle.com/datasets/emmarex/plantdisease
  2. Extract to: agroscan/dataset/PlantVillage/
  3. pip install tensorflow scikit-learn matplotlib seaborn
  4. python train.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime

# ─── TensorFlow imports ───────────────────────────────────────────────────────
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import (
    ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard
)
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score
)

# ─── Config ───────────────────────────────────────────────────────────────────
DATA_DIR    = Path("dataset/PlantVillage")
MODEL_DIR   = Path("model")
REPORTS_DIR = Path("model/reports")
IMG_SIZE    = (224, 224)
BATCH_SIZE  = 32
EPOCHS      = 20       # Increase to 40+ for better accuracy
FINE_TUNE_AT = 100     # Unfreeze layers after this index for fine-tuning
SEED        = 42

# Create dirs
MODEL_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

print(f"TensorFlow version: {tf.__version__}")
print(f"GPU: {tf.config.list_physical_devices('GPU')}")

# ─── Data generators ─────────────────────────────────────────────────────────
print("\n📂 Loading dataset...")

train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2,
    rotation_range=30,
    width_shift_range=0.15,
    height_shift_range=0.15,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    fill_mode='nearest',
)

val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.2,
)

train_gen = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    seed=SEED,
    shuffle=True,
)

val_gen = val_datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation',
    seed=SEED,
    shuffle=False,
)

NUM_CLASSES  = train_gen.num_classes
CLASS_NAMES  = list(train_gen.class_indices.keys())
print(f"✅ Found {train_gen.samples} training samples in {NUM_CLASSES} classes")
print(f"✅ Found {val_gen.samples} validation samples")

# Save class names
import json
with open(MODEL_DIR / "class_names.json", "w") as f:
    json.dump(CLASS_NAMES, f, indent=2)
print("✅ Class names saved to model/class_names.json")

# ─── Model: MobileNetV2 Transfer Learning ─────────────────────────────────────
print("\n🏗️  Building MobileNetV2 model...")

base_model = MobileNetV2(
    input_shape=(*IMG_SIZE, 3),
    include_top=False,
    weights='imagenet',
)
base_model.trainable = False  # Freeze all base layers initially

# Custom classification head
inputs  = tf.keras.Input(shape=(*IMG_SIZE, 3))
x       = base_model(inputs, training=False)
x       = layers.GlobalAveragePooling2D()(x)
x       = layers.Dense(512, activation='relu')(x)
x       = layers.BatchNormalization()(x)
x       = layers.Dropout(0.4)(x)
x       = layers.Dense(256, activation='relu')(x)
x       = layers.Dropout(0.3)(x)
outputs = layers.Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs, outputs, name='AgroScan_MobileNetV2')

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss='categorical_crossentropy',
    metrics=['accuracy', tf.keras.metrics.TopKCategoricalAccuracy(k=3, name='top3_acc')],
)

model.summary()
print(f"\n✅ Model has {model.count_params():,} parameters")
print(f"   Trainable: {sum([np.prod(w.shape) for w in model.trainable_weights]):,}")

# ─── Phase 1: Train head only ─────────────────────────────────────────────────
print("\n🏋️  Phase 1: Training classification head...")

callbacks_phase1 = [
    ModelCheckpoint(
        str(MODEL_DIR / "agroscan_mobilenetv2.h5"),
        monitor='val_accuracy', save_best_only=True, verbose=1,
    ),
    EarlyStopping(monitor='val_accuracy', patience=5, restore_best_weights=True, verbose=1),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6, verbose=1),
    TensorBoard(log_dir=str(REPORTS_DIR / "logs"), histogram_freq=1),
]

history1 = model.fit(
    train_gen,
    epochs=EPOCHS // 2,
    validation_data=val_gen,
    callbacks=callbacks_phase1,
)

# ─── Phase 2: Fine-tuning (unfreeze top layers) ───────────────────────────────
print(f"\n🔧 Phase 2: Fine-tuning from layer {FINE_TUNE_AT}...")

base_model.trainable = True
# Freeze layers before FINE_TUNE_AT
for layer in base_model.layers[:FINE_TUNE_AT]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),  # Much smaller LR
    loss='categorical_crossentropy',
    metrics=['accuracy', tf.keras.metrics.TopKCategoricalAccuracy(k=3, name='top3_acc')],
)

history2 = model.fit(
    train_gen,
    epochs=EPOCHS,
    initial_epoch=history1.epoch[-1],
    validation_data=val_gen,
    callbacks=callbacks_phase1,
)

# ─── Evaluation ───────────────────────────────────────────────────────────────
print("\n📊 Evaluating model...")
val_gen.reset()
loss, acc, top3 = model.evaluate(val_gen, verbose=1)
print(f"\n✅ Validation Accuracy : {acc * 100:.2f}%")
print(f"✅ Top-3 Accuracy      : {top3 * 100:.2f}%")
print(f"✅ Validation Loss     : {loss:.4f}")

# Confusion matrix
print("\n🔍 Generating confusion matrix...")
val_gen.reset()
y_pred_probs = model.predict(val_gen, verbose=1)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = val_gen.classes

# Classification report
report = classification_report(y_true, y_pred, target_names=CLASS_NAMES, output_dict=True)
print("\n📋 Classification Report:")
print(classification_report(y_true, y_pred, target_names=CLASS_NAMES))

# Save report
with open(REPORTS_DIR / "classification_report.json", "w") as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "accuracy": float(acc),
        "top3_accuracy": float(top3),
        "loss": float(loss),
        "per_class": report,
    }, f, indent=2)

# ─── Confusion Matrix Plot ────────────────────────────────────────────────────
print("🎨 Plotting confusion matrix...")
cm = confusion_matrix(y_true, y_pred)

# Abbreviated class names for display
short_names = [n.split("___")[-1].replace("_", " ")[:20] for n in CLASS_NAMES]

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor('#050508')
ax.set_facecolor('#0A0E12')

sns.heatmap(
    cm, annot=True, fmt='d', cmap='YlOrRd',
    xticklabels=short_names, yticklabels=short_names,
    ax=ax, linewidths=0.3, linecolor='#1E2436',
    cbar_kws={'label': 'Count', 'shrink': 0.8},
)
ax.set_title('AgroScan Confusion Matrix — MobileNetV2', color='white', fontsize=14, pad=12)
ax.set_xlabel('Predicted Label', color='#A8C4B8', fontsize=11)
ax.set_ylabel('True Label', color='#A8C4B8', fontsize=11)
ax.tick_params(colors='#A8C4B8', labelsize=8)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(REPORTS_DIR / "confusion_matrix.png", dpi=120, bbox_inches='tight', facecolor='#050508')
print(f"✅ Confusion matrix saved to {REPORTS_DIR}/confusion_matrix.png")

# ─── Training History Plot ────────────────────────────────────────────────────
print("📈 Plotting training history...")

# Merge phase 1 and 2 histories
all_acc     = history1.history['accuracy']     + history2.history['accuracy']
all_val_acc = history1.history['val_accuracy'] + history2.history['val_accuracy']
all_loss    = history1.history['loss']         + history2.history['loss']
all_val_loss= history1.history['val_loss']     + history2.history['val_loss']

epochs_range = range(1, len(all_acc) + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.patch.set_facecolor('#050508')

# Accuracy
ax1.set_facecolor('#0A0E12')
ax1.plot(epochs_range, all_acc,     color='#00E676', linewidth=2, label='Train Acc')
ax1.plot(epochs_range, all_val_acc, color='#00BCD4', linewidth=2, label='Val Acc',   linestyle='--')
ax1.axvline(x=len(history1.history['accuracy']), color='#FFB300', linestyle=':', alpha=0.6, label='Fine-tune start')
ax1.set_title('Model Accuracy', color='white', fontsize=12)
ax1.set_xlabel('Epoch', color='#A8C4B8')
ax1.set_ylabel('Accuracy', color='#A8C4B8')
ax1.tick_params(colors='#A8C4B8')
ax1.legend(facecolor='#0E111A', edgecolor='#1E2436', labelcolor='#A8C4B8')
ax1.set_ylim([0, 1])
ax1.grid(alpha=0.1, color='white')

# Loss
ax2.set_facecolor('#0A0E12')
ax2.plot(epochs_range, all_loss,     color='#FF5252', linewidth=2, label='Train Loss')
ax2.plot(epochs_range, all_val_loss, color='#FF1744', linewidth=2, label='Val Loss', linestyle='--')
ax2.axvline(x=len(history1.history['loss']), color='#FFB300', linestyle=':', alpha=0.6, label='Fine-tune start')
ax2.set_title('Model Loss', color='white', fontsize=12)
ax2.set_xlabel('Epoch', color='#A8C4B8')
ax2.set_ylabel('Loss', color='#A8C4B8')
ax2.tick_params(colors='#A8C4B8')
ax2.legend(facecolor='#0E111A', edgecolor='#1E2436', labelcolor='#A8C4B8')
ax2.grid(alpha=0.1, color='white')

plt.suptitle('AgroScan Training History — MobileNetV2 Transfer Learning', color='white', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(REPORTS_DIR / "training_history.png", dpi=120, bbox_inches='tight', facecolor='#050508')
print(f"✅ Training history saved to {REPORTS_DIR}/training_history.png")

# ─── Summary ─────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  AgroScan Training Complete!")
print("="*60)
print(f"  Model saved    : {MODEL_DIR}/agroscan_mobilenetv2.h5")
print(f"  Val Accuracy   : {acc * 100:.2f}%")
print(f"  Top-3 Accuracy : {top3 * 100:.2f}%")
print(f"  Classes        : {NUM_CLASSES}")
print(f"  Reports dir    : {REPORTS_DIR}/")
print("="*60)
print("\nNext step: python app.py  (runs the web server on port 5050)")
