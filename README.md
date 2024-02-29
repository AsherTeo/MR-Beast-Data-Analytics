# MrBeast Analysis Dashboard

## Overview

This project features a comprehensive analysis dashboard for MrBeast's content. The dashboard, implemented in Python, provides insights into various aspects of MrBeast's videos, engagement metrics, and more. The data is extracted from the YouTube API, and Python is utilized for data wrangling, leveraging the powerful `pandas` library.

The analysis includes statistical insights using the `stats` library, data visualization using `seaborn`, and machine learning utilizing `scikit-learn`. These tools collectively contribute to a thorough exploration and understanding of MrBeast's content landscape.

Additionally, for data cleaning and NLP tasks, the project uses the `nltk` and `strings` libraries. This includes removing stopwords, tokenization, lemmatization, and conducting sentiment analysis in the comment sections. Redundant data, such as non-English words, is filtered out to enhance the quality of the analysis.

The dashboard boasts a user-friendly interface, making it easy for users to explore and interpret the data. Additionally, for enhanced interactivity and visualization, **Power BI** is integrated to create an engaging and insightful dashboard.

## Key Features
- Comprehensive analysis of MrBeast's video content.
- Extraction of data from YouTube API using Python.
- Data wrangling with the `pandas` library.
- Statistical analysis and data visualization.
- Utilization of `nltk` and `strings` libraries for data cleaning and NLP tasks.
- User-friendly interface for easy exploration.

## Objective

The primary objective of this project is to employ machine learning techniques, specifically using `scikit-learn` in Python, to predict the view count of MrBeast's videos. This overarching goal involves leveraging Python as the primary tool for all data-related tasks, including data wrangling, exploratory data analysis (EDA), and the development of predictive models.

### Specific Objectives:

1. **Top 10 Videos Based on View Count:**
   Identify and present the top 10 videos by view count to highlight MrBeast's most popular content.

2. **Analyze the Trend in Video Views Over the Years:**
   Investigate how the number of video views has evolved over the years to understand overall trends.

3. **Explore the Correlation Between Likes, Comments, and Views:**
   Analyze the relationships between likes, comments, and views to uncover potential patterns.

4. **Investigate the Impact of Video Duration on View Count:**
   Examine how the duration of MrBeast's videos affects their view counts.

5. **Examine Mr Beast's Video Upload Frequency Over 12 Years:**
   Study the frequency of MrBeast's video uploads over a 12-year period to identify any patterns or changes.

6. **Identify Frequently Used Words in Mr Beast's Video Titles and Explore Trends:**
   Analyze the titles of MrBeast's videos to identify commonly used words and explore trends in naming conventions.

7. **Assess the Influence of Comments on View Count:**
   Investigate how comments on MrBeast's videos may impact their view counts.

8. **Develop a Machine Learning Model to Predict Video View Count:**
  Utilize machine learning techniques, specifically with `scikit-learn`, to develop a predictive model that accurately estimates the view count of MrBeast's videos based on various features.



## Methodology

### Data Wrangling
Data wrangling is performed using the `pandas` library in Python. This includes cleaning and organizing the raw data obtained from the YouTube API, handling missing values, and ensuring data quality for subsequent analysis.

### Exploratory Data Analysis (EDA)
Exploratory Data Analysis involves utilizing statistical techniques and visualizations to uncover patterns, correlations, and outliers within the dataset. `stats` library and `seaborn` are employed for this phase, providing valuable insights into MrBeast's video metrics.

### Machine Learning
Machine learning techniques, implemented through `scikit-learn`, are utilized to derive predictive models or classifications based on the analyzed data. This includes tasks such as sentiment analysis on comments, predicting engagement metrics, or any other relevant objectives identified during the analysis.

## How to Use
1. [Include step-by-step instructions on how to run or access the dashboard]
2. [Specify any dependencies or prerequisites]

## **Installation**

The code is developed using Python version 3.7.16. If Python is not already installed on your system, you can download it [here](https://www.python.org/downloads/). If your current Python version is lower than 3.7.16, you can upgrade it using the pip package manager. Make sure you have the latest version of pip installed. To install the necessary packages and libraries, execute the following command in the project directory after cloning the repository:

```bash
pip install -r requirements.txt
```
## **DashBoard**
### Summary
![MR Beast Dashboard_1](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/ee98c121-a7ca-4a0c-b0e6-93f8ca874358)

### Exploring the Corrleation between Views, Likes, and Comments
![MR Beast Dashboard_2](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/b5ed9d7a-a844-4779-9cce-43d2d252239e)

### Video Duration Insight
![MR Beast Dashboard_3](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/f8b9ee50-31c4-4c2b-a96d-3ce687487c89)

### Analyzing Model Predictions and Actual Results
![MR Beast Dashboard_4](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/bd147943-6e21-4d61-858c-16468516c4b1)



