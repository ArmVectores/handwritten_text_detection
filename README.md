# About project
This project is to some extent an Armenian adaptation of SHIFT OCR, and the adaptation itself was created by students of the HSE Bachelor's degree in Applied Mathematics - Bashmakov Amir and Shagin Renal under the guidance of David Kagramanyan.
# Armenian Handwritten Text Detection

This repository is dedicated to the project that aims at transforming handwritten Armenian texts into digitally printed text using YOLOv5 neural network model. The core of this project revolves around the application of advanced deep learning techniques to understand and convert handwritten Armenian scripts into their digital equivalents, making it significantly easier to preserve, analyze, and reproduce these texts.

## Project Overview

Handwritten Armenian texts, given their unique script and historical importance, present a fascinating challenge for optical character recognition (OCR) systems. The project uses the YOLOv5 model, renowned for its efficiency and accuracy in object detection tasks, to recognize Armenian handwritten characters. Alongside, we employ Label Studio, a versatile tool for data labeling tasks, to annotate images of the handwritten texts efficiently.

## Getting Started

### Prerequisites

Before diving into this project, you'll need to set up your environment properly. Ensure you have Python 3.8 or higher installed along with pip for managing Python packages.

### Installation

1. Clone the repository
```
    git clone https://github.com/ArmVectores/handwritten_text_detection.git
    cd handwritten_text_detection
```

2. Install the required packages
```
    pip install -r requirements.txt
```

3. Setting up Label Studio for Annotation

Follow the official documentation of Label Studio to install it on your machine: [Label Studio Documentation](https://labelstud.io/guide/#Installation). You'll use Label Studio to label your dataset of Armenian handwritten text images.

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

## License

This project is licensed under [MIT License](LICENSE) - see the LICENSE file for details.

## Contact
For any inquiries or collaborations, please contact [ArmVectores](https://github.com/ArmVectores).


This brief guide outlines the essential steps to get the project up and running. For detailed information on model training, data labeling, and advanced usage scenarios, please refer to the respective official documentation of the tools and libraries used.

Happy handwriting text detection!