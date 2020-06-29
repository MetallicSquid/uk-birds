# uk-birds
A dataset of UK birds, as detected by a Raspberry Pi, camera module and CNN.

## Goal
The aim of this repository is to train an convolutional neural network on a mixture of bird and landscape datasets so that it can detect the presence of a bird in the frame. When a bird is detected, a picture will be taken and a new dataset will be created over time.

## The training data
The model is trained on a combination of datasets:
 *  [Caltech-USDC Birds 200 - A large dataset 200 different species of birds.](http://www.vision.caltech.edu/visipedia/CUB-200.html)
 *  [Landscape Pictures - Dastasets of pictures of natural landscapes.](https://www.kaggle.com/arnaud58/landscape-pictures)
 
In order to train the model, create a directory called `training_dataset` in this repo. Then download and extract the datasets into the directory called `training_dataset`.
