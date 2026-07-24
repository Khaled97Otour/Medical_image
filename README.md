# Medical_image

# Brain MRI Image Processing and 3D Reconstruction

A Python-based project for **brain MRI image analysis**, including:

* Image preprocessing
* Morphological operations
* Brain segmentation
* Tissue clustering
* Statistical analysis
* 3D reconstruction and visualization

This project uses computer vision, machine learning, and 3D visualization techniques to process grayscale MRI brain images.
---
# Installation:
## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

## 2. Environment Setup

This project uses a dedicated Conda environment for medical image processing, brain segmentation, deep learning, and 3D reconstruction.

The environment includes:

- PyTorch with CUDA support
- MONAI for medical image deep learning and U-Net models
- OpenCV for image processing
- Scikit-image for morphology operations and image analysis
- Scikit-learn for machine learning methods (e.g., K-means clustering)
- Open3D for 3D visualization and reconstruction
- Nibabel/SimpleITK for medical image formats
- Scientific Python libraries (NumPy, SciPy, Matplotlib, Pandas)

---

### 1. Install Conda

If Conda is not installed, install Miniconda:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh
```

Restart the terminal and verify:

```bash
conda --version
```

---

### 2. Create a Virtual Environment

Create a dedicated environment for brain segmentation:

```bash
conda create -n brainseg python=3.10
```

Activate the environment:

```bash
conda activate brainseg
```

---

### 3. Install Required Libraries

### Scientific Computing and Image Processing

```bash
conda install -c conda-forge \
numpy \
scipy \
matplotlib \
scikit-learn \
scikit-image \
opencv \
open3d
```

### PyTorch with GPU Support

For NVIDIA GPUs:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### MONAI (Medical AI Framework)

Install MONAI for U-Net and medical image segmentation:

```bash
pip install monai
```

### Additional Medical Imaging Libraries

```bash
pip install nibabel SimpleITK pandas tqdm
```

### Tkinter Support

Required for GUI file selection:

```bash
sudo apt install python3-tk
```

---

### 4. Verify Installation

Run Python:

```bash
python
```

Test the installed libraries:

```python
import torch
import cv2
import numpy as np
import sklearn
import matplotlib
import open3d as o3d
import monai

from skimage.measure import marching_cubes
from monai.networks.nets import UNet

print("All libraries imported successfully")
print("CUDA available:", torch.cuda.is_available())
```

Expected output:

```
All libraries imported successfully
CUDA available: True
```

---

### 5. Project Capabilities

This environment supports:

- Brain MRI preprocessing
- Morphological image processing
- K-means based tissue segmentation
- Deep learning segmentation using U-Net
- MONAI-based medical AI models
- GPU accelerated training and inference
- 3D reconstruction using Marching Cubes
- 3D visualization using Open3D

---

### 6. Environment Information

Recommended configuration:

```
Python      : 3.10
Framework   : PyTorch + MONAI
GPU         : NVIDIA GPU with CUDA support
Environment : Conda (brainseg)
```
## 3. Verify Installation

Run Python and test imports:

import cv2
import torch
import numpy
import sklearn
import open3d
import skimage
import matplotlib

If no errors appear, installation is successful.

---

# Features

## Image Processing

* Read grayscale MRI images
* Convert images into binary masks
* Morphological operations:

  * Dilation
  * Erosion
  * Opening
  * Closing

## Brain Segmentation

* Detect contours
* Extract brain regions
* Remove noise and irrelevant regions

## Tissue Clustering

Uses **K-Means clustering** to separate:

* Background
* Gray matter
* White matter

## Statistical Analysis

Calculates:

* Local mean intensity
* Local variance

Displays statistical plots using Matplotlib.

## 3D Reconstruction

Builds a 3D point cloud model from sequential MRI slices using:

* Marching Cubes
* Open3D visualization

---

# Technologies Used

* Python
* OpenCV
* PyTorch
* NumPy
* Scikit-learn
* Matplotlib
* Open3D
* scikit-image
* Tkinter

---

# Project Structure

```text
project/
│
├── main.py
├── README.md
└── MRI_Images/
    ├── image1.png
    ├── image2.png
    └── ...
```

---

# How It Works

## Single Image Processing

The program allows the user to:

1. Load one MRI image
2. Display the image
3. Segment the brain region
4. Cluster tissues into categories
5. Visualize statistical measurements

## Folder Processing

The user can:

1. Select a folder containing MRI slices
2. Generate a 3D reconstruction
3. Visualize the brain model

---

# Usage

Run the script:

```bash
python main.py
```

---

# Program Workflow

## Step 1 — Select Input Type

```text
Select your process:
'img' for one image
'folder' for a sequence of images
```

---

## Step 2 — Single Image Options

```text
'img'     -> display original image
'seg'     -> display segmented image
'cluster' -> display clustered tissues
```

---

## Step 3 — Folder Options

```text
'0' -> reconstruct original slices
'1' -> reconstruct segmented slices
```

---

# Main Functions

## Morphological Operations

### Dilation

Expands bright regions in the image.

### Erosion

Shrinks bright regions.

### Opening

Removes small noise.

### Closing

Fills small holes.

---

# Segmentation Pipeline

```text
MRI Image
   ↓
Binary Conversion
   ↓
Morphological Opening
   ↓
Contour Detection
   ↓
Region Filtering
   ↓
Segmented Brain
```

---

# Clustering Pipeline

K-Means clustering divides the segmented image into 3 tissue classes:

| Cluster | Description  |
| ------- | ------------ |
| 0       | Background   |
| 1       | Gray Matter  |
| 2       | White Matter |

---

# 3D Reconstruction

The program:

1. Loads sequential MRI slices
2. Builds a 3D volume
3. Applies Marching Cubes
4. Generates a point cloud
5. Displays a 3D brain model

---

# Example Output

## Segmentation

* Binary brain mask
* Isolated brain tissue

## Clustering

* Background visualization
* Gray matter extraction
* White matter extraction

## Statistical Plot

Scatter plots showing:

* Mean intensity
* Variance

## 3D Visualization

Interactive Open3D point cloud rendering.

---

# Notes

* Input images should preferably be:

  * Grayscale
  * Same dimensions
  * Sequential MRI slices for 3D reconstruction

* The segmentation thresholds are manually tuned and may require adjustment depending on the MRI dataset.

---

# Possible Improvements

* Add GUI support
* Improve segmentation using Deep Learning
* Add DICOM support
* Export 3D meshes
* Add volume rendering
* Improve clustering accuracy

---

# Future Work

Potential extensions:

* Tumor detection
* CNN-based tissue classification
* Real-time visualization
* Quantitative MRI analysis

---

# Author

Developed for educational and research purposes in:

* Medical image processing
* Computer vision
* MRI analysis
* 3D reconstruction

---
