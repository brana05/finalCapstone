Software Name

sentiment_analasys

Description

This Python program is a command-line tool that analyzes sentiment in Amazon Consumer Review data obtained from Kaggle. It leverages the following libraries to perform its tasks:

Pandas: Data manipulation and analysis
spaCy: Natural Language Processing (NLP)
TextBlob: Sentiment analysis (optional, if not using spaCy's sentiment analysis)
os: Operating system interaction (for file paths or clearing the screen)
time: Pausing execution.
The program utilizes the en_core_web_sm language model from spaCy for sentiment analysis.

Requirements:

- Python 3.x (https://www.python.org/downloads/)
- Pandas (pip install pandas)
- spaCy (pip install spacy)
- Download the en_core_web_sm language model: python -m spacy download en_core_web_sm
- TextBlob (pip install textblob)
- os
- time

Usage

Make sure that dataset amazon_product_review is included in the same directory as porogram

Run the program:

Open a terminal or command prompt and navigate to the directory containing your program.
Execute the program using sentiment_analasys.py.

Output

The program will analyze the sentiment of reviews in the dataset and display the following information for each review:

Review text
Polarity score (positive or negative sentiment)
Additional data points relevant to your sentiment analysis task.
The output will be printed to the console.

Enhanced Functionality and Error Handling

While the initial task requirements focused on comparing sentiment for two product reviews, I've introduced additional functionality that allows you to select and analyze one to all entries within the provided dataset.
 This flexibility enables the ability to perform more comprehensive sentiment analysis on a larger scale.
 Also it is wraped in basic error handling. 
