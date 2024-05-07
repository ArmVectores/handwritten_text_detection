from setuptools import setup, find_packages

setup(
    name = 'MyProject',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        'ExampleRepo @ git+ssh://git@github.com/example_org/ExampleRepo.git'
    ]
)
