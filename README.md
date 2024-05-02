# About project

This project is to some extent an Armenian adaptation of SHIFT OCR, and the adaptation itself was created by students of the HSE Bachelor's degree in Applied Mathematics - Bashmakov Amir and Shagin Renal under the guidance of David Kagramanyan.

# Project purpose

This repository is dedicated to a project that uses advanced deep learning techniques to the recognition of handwritten Armenian scripts. The purpose of the project is to train the YOLOv8n neural network for the task of word detection in handwritten Armenian texts, which will greatly facilitate the preservation, analysis, processing and reproduction of these texts.

### Prerequisites

Before diving into this project, you'll need to set up your environment properly. Ensure you have Python 3.8 or higher installed along with pip for managing Python packages.

## How to use

```
pip install ultralytics
pip install --upgrade huggingface_hub
pip install arm_text_detection
```

```
from arm_text_detection.detection import Detector

detector = Detector()

res = detector.detect("path/to/your/image")
```

### Preparing Your Dataset

To use this model effectively, you'll need a dataset of Armenian handwritten text images. The images should be clearly readable and contain diverse handwriting styles for better model training.

1. Collect your dataset: Gather a diverse set of handwritten Armenian texts.
2. Label your dataset: Use Label Studio to annotate the dataset. You'll need to define labels for each Armenian character and possibly for common ligatures or word forms.

### Training the Model

Once your dataset is ready and labeled, you can proceed to train the YOLOv5 model on it.

1. Prepare your data: Organize your data and annotations in a format that YOLOv5 expects. The YOLOv5 documentation provides guidelines on how to structure your dataset.

2. Train your model: Use the following command to start the training process:
```
    python train.py --img 640 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt
```
Adjust the parameters according to your dataset size and machine capabilities.

### Evaluating and Using Your Model

After training, evaluate your model's performance using the validation dataset. If you're satisfied with the results, you can use the trained model to convert handwritten Armenian texts into digital text.

## Contribution

Contributions to this project are welcome. Whether it's improving the model's accuracy, expanding the dataset, or enhancing the documentation, your help can make a significant difference.


## Contact
For any inquiries or collaborations, please contact [ArmVectores](https://github.com/ArmVectores).


This brief guide outlines the essential steps to get the project up and running. For detailed information on model training, data labeling, and advanced usage scenarios, please refer to the respective official documentation of the tools and libraries used.

Happy handwriting text detection!