### Very simple Deepfake detector:

The model in this application is VGG19 with [pre-trained weights, h5](https://github.com/fchollet/deep-learning-models/releases/tag/v0.1).

The dataset is available on [Kaggle, follow the link to Hybrid dataset](https://www.kaggle.com/kylewu/hybrid-dataset-v2).
It was assembled using three datasets: [Celebrities](https://www.kaggle.com/jessicali9530/celeba-dataset), [GAN-generated images](https://www.kaggle.com/tunguz/1-million-fake-faces/kernels) and [Deepfake competition dataset](https://www.kaggle.com/c/deepfake-detection-challenge/).

### Installation
Weights were uploaded with Git LFS, make sure you have Git LFS installed and initialised, follow the [instruction](https://git-lfs.github.com/) before you clone the project.

The GUI works under PySide2, there might be a conflict of OpenCV and PySide libraries; you have to install OpenCV with a particular version to make it work stably, use the following:
```sh
$ pip install opencv-python==4.1.0.25
```
