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
- Application of machine learning techniques, specifically with `scikit-learn`, for predictive modeling.
- User-friendly interface for easy exploration.

## Objective

The primary objective of this project is to employ machine learning techniques, specifically using `scikit-learn` in Python, to predict the view count of MrBeast's videos. This overarching goal involves leveraging Python as the primary tool for all data-related tasks, including data extraction, data wrangling, exploratory data analysis (EDA), and the development of predictive models.

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

### 1) Data Extraction
In the initial phase, data extraction from the YouTube API is executed using Python. The process involves utilizing the `googleapiclient` libraries to establish a connection with the API. This connection facilitates the retrieval of essential information, encompassing the video's Title, publishedAt timestamp, viewCount, likeCount, commentCount, duration, and a comprehensive set of 1000 comments for all of MrBeast's video content.

### 2) Data Wrangling
Data wrangling is executed through the use of the `pandas` library in Python. This process encompasses several crucial steps, starting with the cleaning and organization of raw data obtained from the YouTube API. Tasks involve handling missing values, adjusting the data types of each feature to their correct formats, and implementing specific text manipulations.

Text tokenization is performed, and any tokens beginning with '$' are replaced to convey monetary values. For instance, '$ 800,000' is transformed into the identifier 'money'. Similarly, numeric values are standardized, with both '1' and '100' represented as 'number' for consistency.

Further refinement involves the removal of stop words to enhance the relevance of the textual content. Additionally, lemmatization is applied to streamline words to their base forms. To ensure the text is clean and focused, any symbols and non-English characters are removed.

To gain deeper insights, semantic analysis is employed, classifying sentiments into percentages of positivity, neutrality, and negativity. This multifaceted approach ensures the data is refined, structured, and enriched, setting the stage for more comprehensive and insightful analyses.

### 3) Exploratory Data Analysis (EDA)
Exploratory Data Analysis (EDA) utilizes statistical techniques and visualizations, employing the `stats` library and `seaborn` to reveal patterns and outliers in MrBeast's video metrics. Skewness and Shapiro tests assess normality; if not observed, a log transformation is applied. If non-normality persists (p-values < 0.05), non-parametric models like Decision Trees and Random Forests are recommended for machine learning analyses. The top 10 videos, based on view count and considering view count per day, are identified to ensure fairness in comparisons across different upload times. Subsequently, relationships between view count, like count, and duration are examined, and durations are grouped for enhanced visualization. The analysis also involves determining the most frequent words in video titles and converting categorical features into one-hot encoding, while removing redundant features.

### 4) Machine Learning Analysis

The process begins with the standardization of numerical data using the Standard Scaler. This step ensures that all numerical features are normalized to a consistent range, preventing certain features from dominating others during model training. A variety of non-parametric regression models, including Decision Tree, Random Forest, XGBoost, and others, are considered for predicting numerical metrics like view count or engagement ratios.

The dataset undergoes 10-Fold cross-validation to thoroughly assess the model's performance across different subsets of the data, providing a robust evaluation. The performance of each model is then evaluated using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared score. These metrics provide insights into how well the models capture the variance in the target variable and make accurate predictions.

To further enhance the models, a grid search is employed to fine-tune hyperparameters. This systematic search over a predefined hyperparameter space helps identify the optimal set of hyperparameters for each model. The process involves exploring different combinations of hyperparameters to maximize predictive performance.

After hyperparameter tuning, the models are re-evaluated using the same metrics (MSE, MAE, R-squared score). This step ensures that the adjustments made during hyperparameter tuning lead to improvements in model performance.

Finally, the best model is determined based on the lowest MSE score. Ensemble models, including Ensemble without hyperparameter tuning, Random Forest with hyperparameter tuning, and Extra Tree with hyperparameter tuning, emerge as the top contenders.

<div style="display: flex; justify-content: space-between;">

### Before Hyperparameter Tuning  vs  After Hyperparameter Tuning

| Model            | MSE   | MAE   | R-squared |         | Model            | MSE   | MAE   | R-squared |
|------------------|-------|-------|-----------|         |------------------|-------|-------|-----------|
| Decision Tree    | Value | Value | Value     |         | Decision Tree    | Value | Value | Value     |
| Random Forest    | Value | Value | Value     |         | Random Forest    | Value | Value | Value     |
| XGBoost          | Value | Value | Value     |         | XGBoost          | Value | Value | Value     |
| Ensemble         | Value | Value | Value     |         | Ensemble         | Value | Value | Value     |
| Random Forest    | Value | Value | Value     |         | Random Forest    | Value | Value | Value     |
| Extra Tree       | Value | Value | Value     |         | Extra Tree       | Value | Value | Value     |

### After Hyperparameter Tuning

| Model            | MSE   | MAE   | R-squared |
|------------------|-------|-------|-----------|
| Decision Tree    | Value | Value | Value     |
| Random Forest    | Value | Value | Value     |
| XGBoost          | Value | Value | Value     |
| Ensemble         | Value | Value | Value     |
| Random Forest    | Value | Value | Value     |
| Extra Tree       | Value | Value | Value     |

</div>

### 5) Conclusion

## **Installation**

The code is developed using Python version 3.7.16. If Python is not already installed on your system, you can download it [here](https://www.python.org/downloads/). If your current Python version is lower than 3.7.16, you can upgrade it using the pip package manager. Make sure you have the latest version of pip installed. To install the necessary packages and libraries, execute the following command in the project directory after cloning the repository:

```bash
pip install -r requirements.txt
```
## **DashBoard**
The project's interactive dashboard serves as a central hub for exploring and interpreting the comprehensive analysis of MrBeast's content. Developed using Power BI, the dashboard offers users a visually engaging and user-friendly interface, making it easy to derive meaningful insights from the data.

### Summary
The summary section offers a quick snapshot of essential metrics, providing a bird's-eye view of MrBeast's overall video landscape. It includes key statistics such as total views, likes, comments, and video count. The visual representation facilitates an instant understanding of the channel's performance.

![MR Beast Dashboard_1](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/ee98c121-a7ca-4a0c-b0e6-93f8ca874358)

### Exploring the Correlation between Views, Likes, and Comments
Dive into the relationships between views, likes, and comments with this interactive visualization. Uncover patterns and correlations that provide insights into viewer engagement and content reception.

![MR Beast Dashboard_2](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/b5ed9d7a-a844-4779-9cce-43d2d252239e)

### Video Duration Insight
Explore the impact of video duration on view counts. This visualization allows you to analyze how the length of MrBeast's videos influences their popularity and viewer retention.

![MR Beast Dashboard_3](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/f8b9ee50-31c4-4c2b-a96d-3ce687487c89)

### Analyzing Model Predictions and Actual Results
Delve into the world of machine learning predictions with this section. Compare the predictions generated by the machine learning model, developed using `scikit-learn`, against the actual view counts. Gain insights into the model's accuracy and its ability to predict video performance.

![MR Beast Dashboard_4](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/bd147943-6e21-4d61-858c-16468516c4b1)



