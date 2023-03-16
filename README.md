# DS-4002-Project2

## Contents of the Repository

This repository includes all of the necessary files related to the first DS 4002 project for our group, The Swifties. This README.md file contains an overview of what is included in each of the three folders: SRC, Data, and Figures. The LICENSE.md file explains to a visitor the terms under which they may use and cite this repository. The SRC folder contains all source code for the project. The Data folder contains all of the data for the project. Lastly, the Figures folder contains all figures generated over the course of the project.

## SRC

We pulled the source data from Kaggle. It includes all of Taylor Swift's songs released during the time frame 2006-2017. It also includes the lyrics, song name, album name, and year of release.

### Installing/Building Code

We downloaded the data as a .csv file and cleaned it for use in R. Make sure the data is available and accessible in the same working directory as the file, and make any neccessary changes to the file path in order for the dataset to be loaded into RStudio on your device.

### Using Code

This code can be used by opening each .R or .Rmd file within RStudio, version 2022.12.

## Data

#### Data Dictionary

| Folder Name         | Data Type     | Description |
| ------------------- | ------------- | ----------- |
| test/Covid          | jpeg, jpg, png| This folder contains jpeg, jpg, and png images of chest x-rays of patients with COVID-19 for testing a model against. |
| test/Normal         | jpeg          | This folder contains jpeg images of chest x-rays of healthy patients for testing a model against.|
| test/Viral Pnemonia | jpeg          | This folder contains jpeg images of chest x-rays of patients with Viral Pneumonia for testing a model against.|
| train/Covid         | jpeg, jpg, png| This folder contains jpeg, jpg, and png images of chest x-rays of patients with COVID-19 for training a model. |
| train/Normal        | jpeg          | This folder contains jpeg images of chest x-rays of healthy patients for training a model.|
| train/Viral Pnemonia| jpeg          | This folder contains jpeg images of chest x-rays of patients with Viral Pneumonia for training a model. |

#### Link to Data

Our dataset can be found [here](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset) [1].

#### Relevant Notes About Data

There are several significant notes about our dataset. Firstly, it is important to note that it only contains lyrics from Taylor Swift's first six albums, not her entire discography. This led to our group adjusting our hypothesis and research question accordingly. Additionally, it is important to note that the dataset breaks up lyrics by line in each song, so some data aggregation will be necessary in order to use each song as individual data points.

## Figures 

| Figure      | Description | Takeaways   |
| ----------- | ----------- | ----------- |
| Romance:CountryRatioGraph.png| This graph has each Taylor Swift song plotted with the year of release on the x-axis and it's romance-to-country ratio on the y-axis. It also includes a line of best fit.| The line of best fit having a positive slope confirms our hypothesis that the lyrics of Taylor Swift's songs have shifted from being more aligned with the country theme to more aligned with the romance theme. |
| album.Romance:Country.png |  This graph has each Taylor Swift album plotted with the year of release on the x-axis and it's romance-to-country ratio on the y-axis. It also includes a line of best fit. | The line of best fit having a positive slope confirms our hypothesis that the lyrics of Taylor Swift's songs have shifted from being more aligned with the country theme to more aligned with the romance theme. |

## References

[1] Raikote, Pranav, “Covid-19 Image Dataset,” Kaggle.com, CC BY-SA 4.0, 2020. [Online]. Available: https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset. [Accessed March 14, 2023].

Our submission for M1 can be found [here](https://docs.google.com/document/d/15BI0JMWRXRKFiejG8Nu_kt_VcEqPVRjsSN_60aouXlg/edit?usp=sharing).

Our submission for M2 is linked [here](https://docs.google.com/document/d/1CNDYayc-ehutT4BBa86Op7M2H-f36dQVTdlzm7_qeuM/edit?usp=sharing).
