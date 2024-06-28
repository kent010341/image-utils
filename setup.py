from setuptools import setup, find_packages

setup(
    name='image-utils-package',
    version='0.1.0',
    description='A package for image processing utilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kent010341',
    author_email='kent010341@gmail.com',
    url='https://github.com/kent010341/image-utils',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'image-utils=image_utils.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
