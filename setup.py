from setuptools import setup, find_packages

setup(
    name="flask-ner",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'spacy',
        'pytest',
        'selenium',
    ],
    python_requires='>=3.6',
)
