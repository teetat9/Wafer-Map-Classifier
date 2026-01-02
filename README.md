# Semiconductor Wafer map Detect Pattern Classification

Classifying defect patterns in semiconductor wafer maps using deep learning technique.

## Environment
- OS: Ubuntu 22.04 (WSL2)
- GPU: NVIDIA GeForce RTX 4060
- Framework: Tensorflow (GPU support using WSL2)
    - TensorFlow version: 2.20.0
    - CUDA version: 12.5.1

## Dataset
- [WM-811K wafer map](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map/data)
- 9 defect patterns: Center, Donut, Edge-Loc, Edge-Ring, Loc, Random, Scratch, Near-Full, None

## Approach
Following methodology from [Wafer Defect Classification](https://github.com/SECQUOIA/wafer-defect-classification), implementing step-by-step to understand semiconductor defect detection.

## Result
Received *95.1%* accuracy on the validating data. Other evaluation metrics also show great performance.

## Progress Log
- [x] 01/01/2026: Loaded dataset, analyze the dataset and understand it, preprocess the data by sorting out unlabeled data and make numerical categories.
- [x] 02/01/2026: Preprocess the data by oversampling the data to reduce bias, resize the data to make them all equal, normalize the data, construct CNN pipeline, setting the parameters, and train the model. Finally, use evaluation metrics to evaluate the model performance.

## References
- Methodology: https://github.com/SECQUOIA/wafer-defect-classification
- Dataset: WM-811K (MIR Lab, National Chiao Tung University)
