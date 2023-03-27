# DS-4002-Project2

## Contents of the Repository

This repository includes all of the necessary files related to the second DS 4002 project for our group, The Swifties. This README.md file contains an overview of what is included in each of the three folders: SRC, DATA, and FIGURES. The LICENSE.md file explains to a visitor the terms under which they may use and cite this repository. The SRC folder contains all source code for the project. The DATA folder contains all of the data for the project. Lastly, the FIGURES folder contains all figures generated over the course of the project.

## SRC

We pulled the source data from Kaggle. It includes images of chest X-rays of patients with COVID-19, patients with viral pnemonia, and healthy lungs. The dataset consists of six different directories, split by recommending testing and training data, each containing a directory for each diagnosed condition.

### Installing/Building Code

We downloaded the data as a collection of image files and cleaned it for use in Python. Make sure the data is available and accessible in the same working directory as the file, and make any neccessary changes to the file path in order for the dataset to be available on your device.

### Using Code

This code can be used by running py .\example.py using Python version 3.11.2.

## Data

#### Data Dictionary

| Folder Name         | Data Type     | Description |
| ------------------- | ------------- | ----------- |
| test/Covid          | jpeg, jpg, png| This folder contains jpeg, jpg, and png images of chest X-rays of patients with COVID-19 for testing a model against. |
| test/Normal         | jpeg          | This folder contains jpeg images of chest X-rays of healthy patients for testing a model against.|
| test/Viral Pnemonia | jpeg          | This folder contains jpeg images of chest X-rays of patients with Viral Pneumonia for testing a model against.|
| train/Covid         | jpeg, jpg, png| This folder contains jpeg, jpg, and png images of chest X-rays of patients with COVID-19 for training a model. |
| train/Normal        | jpeg          | This folder contains jpeg images of chest X-rays of healthy patients for training a model.|
| train/Viral Pnemonia| jpeg          | This folder contains jpeg images of chest X-rays of patients with Viral Pneumonia for training a model. |

#### Link to Data

Our dataset can be found [here](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset) [1].

#### Relevant Notes About Data

It is important to note that the dataset only contains pictures from those affected by COVID-19, Viral Pneumonia, or those unaffected by disease, not people affected by other diseases involving the lungs. This is what caused us to limit our model to these three categories.

## Figures 

| Figure      | Description | Takeaways   |
| ----------- | ----------- | ----------- |
| ConfusionMatrixCOVID.png | This is a table of the confusion matrix of our k-means clustering model.| From this confusion matrix, we can see that most of the miss classified images are COVID and Normal images, but does misclassify any normal/ healthy lungs as COVID, meaning that a false positive result would not be likely. |

## References

[1] Raikote, Pranav, “Covid-19 Image Dataset,” Kaggle.com, CC BY-SA 4.0, 2020. [Online]. Available: https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset. [Accessed March 14, 2023].

Our submission for M1 can be found [here](https://docs.google.com/document/d/15BI0JMWRXRKFiejG8Nu_kt_VcEqPVRjsSN_60aouXlg/edit?usp=sharing).

Our submission for M2 is linked [here](https://docs.google.com/document/d/1CNDYayc-ehutT4BBa86Op7M2H-f36dQVTdlzm7_qeuM/edit?usp=sharing).
