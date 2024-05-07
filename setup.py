from setuptools import setup, find_packages

setup(
    name = 'handwritten_text_detection',
    version = '1.0.1',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        'handwritten_text_detection @ git+ssh://git@github.com:ArmVectores/handwritten_text_detection.git'
    ]
)
