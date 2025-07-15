from setuptools import setup, find_packages

setup(
    name='multilabel-longtail-classifier',
    version='1.0.0',
    description='Improving multilabel deep learning models for long-tail distributions (ODIR5K case study)',
    author='Prashant Mishra',
    author_email='prashant66m@gmail.com',
    url='https://github.com/starkgit91/multilabel-eye-disease',
    packages=find_packages(),
    install_requires=[
        'torch>=1.13.0',
        'torchvision>=0.14.0',
        'scikit-learn>=1.2.0',
        'matplotlib>=3.6.0',
        'seaborn>=0.12.0',
        'albumentations>=1.2.0',
        'pandas>=1.4.0',
        'numpy>=1.22.0',
        'tqdm>=4.64.0',
        'wandb>=0.15.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)