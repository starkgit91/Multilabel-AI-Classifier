# 📊 Improving Multilabel Deep Learning Models for Classes with Long-Tail Distribution

This project is part of my **B.Tech Major Project** at NIT Andhra Pradesh, focused on enhancing multi-label classification performance for datasets exhibiting severe **long-tail class imbalance**.

---

## 🧠 Problem Statement

Real-world medical datasets often suffer from:
- **Long-tailed label distribution** (i.e., many rare classes with few samples)
- **Multi-label structure** (an image can belong to multiple diseases)
- **Bias towards frequent classes** in standard training approaches

Our goal is to **design and evaluate deep learning models** that address this imbalance using both **architecture-level** and **loss-level** improvements.

---

## 🔬 Project Goals

- ✅ Evaluate popular architectures: `InceptionV3`, `ResNet-50`, `VGG16`
- ✅ Implement **long-tail mitigation strategies**:
  - Reweighted Losses (e.g., focal loss, class-balanced loss)
  - Oversampling / Class-balanced sampling
- ✅ Explore **Self-Supervised Learning** for better feature representations
- ✅ Fine-tune models on **ODIR-5K** (Ocular Disease Intelligent Recognition)
- ✅ Improve mAP, F1-score especially on rare classes

---

## 🧪 Dataset: ODIR-5K

- 🩺 **ODIR-5K** is a benchmark medical imaging dataset from eye clinics
- Contains retinal images from patients with multiple diseases
- **Multilabel setting**: each image has 1 or more disease labels
- Total: 5000 images / 8 classes (including rare diseases like DR, AMD)

---

## 🏗️ Architecture Used

| Model           | Backbone      | Pretrained | Strategy         |
|----------------|---------------|------------|------------------|
| Baseline        | InceptionV3   | ✔️ ImageNet | BCE Loss         |
| Improved        | ResNet-50     | ✔️ ImageNet | CB Loss + Aug    |
| Advanced        | InceptionV3   | ✔️ ImageNet | SSL + Class-Bal  |

---

## ⚙️ Techniques Implemented

- 📐 BCEWithLogitsLoss (Baseline)
- 🔄 Class-balanced Loss Function
- 🧪 Focal Loss and LDAM Loss
- 🔁 Over-sampling rare classes
- 🧠 Self-Supervised Learning (SimCLR)
- 📈 mAP, macro/micro F1 evaluation

---

## 📊 Results (summary)

| Model              | F1 Score | mAP    | Recall (Rare) |
|-------------------|----------|--------|----------------|
| InceptionV3        | 71.2%    | 68.5%  | 49.7%           |
| ResNet50 + CB      | 76.9%    | 73.4%  | 63.3%           |
| InceptionV3 + SSL  | **79.8%** | **76.5%** | **66.7%**     |

---

## 🧰 Tech Stack

- 🐍 Python 3.9
- 🧠 PyTorch
- 📦 scikit-learn, Albumentations
- 📊 Matplotlib / Seaborn for visualization
- 🪪 Weights & Biases for experiment tracking

---

## 🧪 Jupyter Notebook

This repo contains:
- `DL_InceptionV3.ipynb` – core training notebook with preprocessed ODIR5K features
- Code for model building, training loops, validation
- Evaluation metrics and confusion matrix

---

## ✍️ Author

**Prashant Mishra**  
AI + ML + Deep Learning Enthusiast  
[GitHub: starkgit91](https://github.com/starkgit91) | [LinkedIn](https://linkedin.com/in/prashant-mishra-976708157/)  

---

## 📌 To Run

```bash
git clone https://github.com/starkgit91/multilabel-eye-disease.git
cd multilabel-eye-disease
jupyter notebook DL_InceptionV3.ipynb
```

---

## 📈 Future Work

- ✨ Incorporate Vision Transformers (ViT)
- 🧠 Try zero-shot models like CLIP for rare labels
- ⏱ Optimize inference pipeline for deployment
