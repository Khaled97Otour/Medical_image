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

## 2. Create a Virtual Environment (Recommended)
python -m venv venv
Activate Environment

### Windows:

venv\Scripts\activate

### Mac/Linux:

source venv/bin/activate
## 3. Install Required Libraries

### Install all dependencies using pip:

pip install numpy
pip install opencv-python
pip install matplotlib
pip install scikit-learn
pip install scikit-image
pip install open3d
pip install torch
## 4. (Optional) Install Everything at Once
pip install numpy opencv-python matplotlib scikit-learn scikit-image open3d torch
## 5. Verify Installation

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

# Installation

## Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

## Install Dependencies

```bash
pip install torch
pip install opencv-python
pip install numpy
pip install scikit-learn
pip install matplotlib
pip install scikit-image
pip install open3d
```

Tkinter usually comes preinstalled with Python.

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
