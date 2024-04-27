# MrBeast Analysis with Dashboard(Below)

## Table of Contents

1) [Overview](#overview)
2) [Objective](#objective)
3) [Key Features](#key-features)
4) [Specific Objectives](#specific-objectives)
5) [Methodology](#methodology)
6) [Result](#result)
7) [Hypothesis Overview](#hypothesis-overview)
8) [Installation](#Installation)
9) [DashBoard- Power BI](#dashBoard-Power-BI)

   
## Overview

This project features a comprehensive analysis dashboard for MrBeast's content. The dashboard, implemented in Power Bi , provides insights into various aspects of MrBeast's videos, engagement metrics, and more. The data is extracted from the YouTube API, and Python is utilized for data wrangling, leveraging the powerful `pandas` library.

The analysis includes statistical insights using the `stats` library, data visualization using `seaborn`, and machine learning utilizing `scikit-learn`. These tools collectively contribute to a thorough exploration and understanding of MrBeast's content landscape.

Additionally, for data cleaning and NLP tasks, the project uses the `nltk` and `strings` libraries. This includes removing stopwords, tokenization, lemmatization, and conducting sentiment analysis in the comment sections. Redundant data, such as non-English words, is filtered out to enhance the quality of the analysis.

The dashboard boasts a user-friendly interface, making it easy for users to explore and interpret the data. Additionally, for enhanced interactivity and visualization, **Power BI** is integrated to create an engaging and insightful dashboard.

## Objective

The primary objective of this project is to employ machine learning techniques, specifically using `scikit-learn` in Python, to predict the view count of MrBeast's videos. This overarching goal involves leveraging Python as the primary tool for all data-related tasks, including data extraction, data wrangling, exploratory data analysis (EDA), and the development of predictive models.

## Key Features

- Comprehensive analysis of MrBeast's video content.
- Extraction of data from YouTube API using Python.
- Data wrangling with the `pandas` library.
- Statistical analysis and data visualization.
- Utilization of `nltk` and `strings` libraries for data cleaning and NLP tasks.
- Application of machine learning techniques, specifically with `scikit-learn`, for predictive modeling.
- User-friendly interface for easy exploration.

## Specific Objectives:

<details>
  <summary>Specific Objectives</summary>
   
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

</details>

## Methodology

<details>
  <summary>Methodology</summary>
   
### 1) Data Extraction
In the initial phase, data extraction from the YouTube API is executed using Python. The process involves utilizing the `googleapiclient` libraries to establish a connection with the API. This connection facilitates the retrieval of essential information, encompassing the video's Title, publishedAt timestamp, viewCount, likeCount, commentCount, duration, and an extensive set of comments. However, due to YouTube API restrictions, a small subset of 1000 comments is used for each video. This limitation ensures compliance with API constraints while still providing a representative sample for analysis and insights.

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

</details>

## Result

### Before Hyperparameter Tuning 

| Model                  | MSE   | MAE   | R-squared |
|------------------|-------|-------|-----------|
| Ensemble               | 0.016561	| 0.084947 | 0.659332  |
| Extra Tree             | 0.016672 | 0.086039 | 0.647378  |
| Random Forest          | 0.016847 |0.085615  | 0.682933  |
| Gradient Boosting	    | 0.018175 | 0.092537 | 0.620210  |
|     XGB	             | 0.018462 | 0.090461 | 0.644267  |
|     LGM	             | 0.018984	| 0.093208 | 0.616331  |
|    Decision Tree       | 0.029395 | 0.115334 | 0.336514  |

### After Hyperparameter Tuning

| Model                  | MSE   | MAE   | R-squared |
|------------------|-------|-------|-----------|
| Ensemble               | 0.016481	| 0.084852 | 0.661702  |
| Extra Tree             | 0.016602 | 0.086503 | 0.647167  |
| Random Forest          | 0.016835 | 0.085577 | 0.682226  |
| Gradient Boosting	    | 0.018492	| 0.092919 | 0.611793  |
|     XGB	             | 0.017836	| 0.090079 | 0.650330  |
|     LGM	             | 0.019296	| 0.091354 | 0.626575  |
|    Decision Tree       | 0.020561	| 0.101062 | 0.633439  |

## Example of Testing Dataset

Example of Testing Dataset with Actual View Count and Target View Count

| Video title                                          | NLP-Processed Dataset                     | Actual View count   | Target View count |
|------------------|-------|-------|-----------|
|    What Is Youtube Terms Of Service?????	          | service term youtube	                     | 4.384400e+04  | 4.745563e+04  |
|    WORLD'S FIRST BLACK OPS 3 GUN SYNC!!              | black gun number op sync world	         |5.664100e+04   | 5.356425e+04  |
|    Battle Pirates, Hellstrike vs Epic Base!		    | base battle epic hellstrike pirate vs		| 5.394500e+04  | 5.393675e+04  |
|    Leaving For 7 Days                                | day leave number                          | 4.636800e+04	 | 4.743633e+04  |
|    Last To Leave Ramen Noodle Pool Wins $20,000		 | leave money noodle pool ramen win	      | 7.227836e+07  | 7.115062e+07  |

## Hypothesis Overview

<details>
  <summary>Hypothesis Overview</summary>
  
- Monetary values and numerical figures are the most frequently used words in the video titles.
- Among the top 10 videos by view count, six of them involve monetary aspects, including giving, spending, and keeping money
- View counts started rising in 2017, coinciding with the year MR. Beast initiated the use of monetary values over $10 000 in his video titles, exemplified by titles like 'Giving My Mom $100,000 (Proudest Day of My Life)' and 'Tipping Pizza Delivery Guys $10,000'.
- Additionally, in 2017, he posted 7 out of 10 videos with durations exceeding 100 minutes, such as 'Reading The Longest English Word (190,000 Characters)' and 'I Counted To 100,000!'
- Videos lasting less than 1 minute have the highest average view counts, suggesting that the audience prefers shorter videos over longer ones.
- During the period from 2012 to 2014, the correlation between Views, Likes, and Comments was notably high, with Views vs Likes at 0.94, Views vs Comments at 0.96, and Likes vs Comments at 0.97. However, as the years progressed, the correlations between Views vs Comments and Likes vs Comments experienced a significant decrease.
- Starting from 2015, MrBeast began uploading videos that are less than a minute long. This has noticeably impacted the correlation between Views vs Comments and Likes vs Comments, suggesting that users watching shorter videos may be less inclined to leave comments
- Starting from 2019, Mr. Beast predominantly uploads videos on Saturdays.
- With a limited sample size of 1000 comments per video, the sentiment analysis suggests that, on average, the majority of comments are neutral (80%), while 16% are positive, and only a minimal 4% are negative.
- The video titled 'Dude Perfect 4.0 - We Are Totally Better' stands out with the highest percentage of negative comments at 0.2%. Examples of negative remarks include expressions like 'you suck', 'y'all are so fake', 'Whole video is fake', 'Go to hell ya suckers'
  
</details>

## **Installation**

<details>
  <summary>Installation</summary>
  
The code is developed using Python version 3.7.16. If Python is not already installed on your system, you can download it [here](https://www.python.org/downloads/). If your current Python version is lower than 3.7.16, you can upgrade it using the pip package manager. Make sure you have the latest version of pip installed. To install the necessary packages and libraries, execute the following command in the project directory after cloning the repository:

```bash
pip install -r requirements.txt
```
  </details>
  
## **DashBoard - Power BI**
The project's interactive dashboard serves as a central hub for exploring and interpreting the comprehensive analysis of MrBeast's content. Developed using Power BI, the dashboard offers users a visually engaging and user-friendly interface, making it easy to derive meaningful insights from the data.

### Summary
The summary section offers a quick snapshot of essential metrics, providing a bird's-eye view of MrBeast's overall video landscape. It includes key statistics such as total views, likes, comments, and video count. The visual representation facilitates an instant understanding of the channel's performance.

![Summary (2)](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/e4abfeb1-f4b5-4b96-9082-14cb82dacaa4)

### Exploring the Correlation between Views, Likes, and Comments
Dive into the relationships between views, likes, and comments with this interactive visualization. Uncover patterns and correlations that provide insights into viewer engagement and content reception.

![Exploring the Correlation between Views, Likes, and Comments](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/2c804dc1-cb74-4b8b-8b26-f71b7707cc2a)

### Video Duration Insight
Explore the impact of video duration on view counts. This visualization allows you to analyze how the length of MrBeast's videos influences their popularity and viewer retention.

![Video Duration Insight](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/ad397de0-5535-454b-92a9-3a6ad71f2571)

### Analyzing Model Predictions and Actual Results
Delve into the world of machine learning predictions with this section. Compare the predictions generated by the machine learning model, developed using `scikit-learn`, against the actual view counts. Gain insights into the model's accuracy and its ability to predict video performance.

![Analyzing Model Predictions and Actual Results](https://github.com/AsherTeo/MR-Beast-Data-Analytics/assets/78581569/cfb376af-4272-47af-859a-008d1c2dca82)



