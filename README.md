# About project

This project is to some extent an Armenian adaptation of SHIFT OCR, and the adaptation itself was created by students of the HSE Bachelor's degree in Applied Mathematics - Bashmakov Amir and Shagin Renal under the guidance of David Kagramanyan.

# The purpose of the project
This repository is dedicated to a project that uses advanced deep learning techniques to recognize handwritten Armenian fonts. The aim of the project is to train the YOLOv8n neural network to recognize words in handwritten Armenian texts, and since this language is not used on the Internet and translators cannot be found anywhere, recognition will greatly facilitate the preservation, analysis, processing and reproduction of these texts.

# Background
Before you start working on this project, you need to set up your environment correctly. Make sure that you have Python version 3.8 or higher installed, as well as pip for managing Python packages.

## How to use
### To download the repository
```
pip install ultralytics
pip install --upgrade huggingface_hub
pip install https://github.com/ArmVectores/handwritten_text_detection/archive/master.zip
or
pip install https://github.com/ArmVectores/handwritten_text_detection/zipball/master
or
pip install https://github.com/ArmVectores/handwritten_text_detection/tarball/master
or
pip install git+ssh://git@github.com:ArmVectores/handwritten_text_detection.git
or
pip install git+https://github.com/ArmVectores/handwritten_text_detection.git
or
pip install git+https://github.com/ArmVectores/handwritten_text_detection.git
```

### To work with the program

```
#to display the coordinates of words
detector=Detector()
boxes=detector.detect("path/to/your/image")
print(boxes)
```
```
#to display the words themselves
words=detector.extract_words("path/to/your/image",boxes)
```

### Preparing your dataset

To use this model effectively, you will need a set of handwritten text images in Armenian. The images should be well readable to get the best result.


### Evaluating and using our model

You can evaluate the performance of our model using a set of validation data. If you are satisfied with the results, you can use a trained model to convert handwritten Armenian texts into digital text.

## Contribution

Contributions to this project are welcome. Whether it's improving the model's accuracy, expanding the dataset, or enhancing the documentation, your help can make a significant difference.


## Contact
For any inquiries or collaborations, please contact [ArmVectores](https://github.com/ArmVectores).


This brief guide outlines the essential steps to get the project up and running. For detailed information on model training, data labeling, and advanced usage scenarios, please refer to the respective official documentation of the tools and libraries used.
