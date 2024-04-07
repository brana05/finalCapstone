#importing libraries that will be in use for the task 
import spacy
import pandas as pd 
import numpy as np 
from textblob import TextBlob
import os
import time

# -----------Functions :----------------

# Text preprocess function 
# this function will remove all stop words and punctiation
# at the same time it will do lemmanization of the words

def preprocess (text):
    doc = nlp(text.lower().strip())
    processed_text=[token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return ' '.join(processed_text)

# end of preprocess

# Sentiment analasys function

def get_sentiment(text):
    blob=TextBlob(text)
    return blob.sentiment.polarity

#get number of entries to analyze  function with error handling.

def get_number_of_entries(max):
    while True:
        try:
            number = int (input(f'Please enter number of elements you would like to analyze \n max number of elements = {max}: '))
            if 0<=number <=max:
                #clear screen
                os.system('cls' if os.name == 'nt' else 'clear')
                return number
            else :
                print (f"Number must be between 0 and {max}")
                #pause for 5 sec during warning that choice is incorect
                time.sleep(5)
        except ValueError: 
            print("Please enter a number !")
            time.sleep(5)
            #clear screen
        os.system('cls' if os.name == 'nt' else 'clear') #clear screen works on most OS's

# ------------End of Functions----------

# Initialising NLP 

nlp = spacy.load('en_core_web_sm')


#importing Amazon dataset 
# clear screen 
os.system('cls' if os.name == 'nt' else 'clear') #clear screen works on most OS's
print("Importing dataset !")
df=pd.read_csv('amazon_product_reviews.csv')

#
#Now I will create sub data frames with data that is needed for analasys 
# and data presentation
# df_subset is used for presentation at the later stage
#
print("Creating Subset!")
subset_columns=['name','reviews.text','reviews.rating']
df_subset=df[subset_columns]

#
# now I will clear all NaN entries in the  Data set if they exist
#Load all nan containing data lines in df

nan_columns=df_subset.isnull().any()

#calculate how many nan containing lines are present in the data set

nan_number=nan_columns.sum()
print(f'Number of NaNlines :{nan_number}')
print("Conditioning dataset by removing stop words punctiation and NaN entries !")
print(" ")
#remove all of the lines with nan if needed 
if nan_number>0:
    df_subset.dropna(inplace=True, axis=0)

# review_text is subset of df that has only review data 
    
review_text = df_subset['reviews.text']

#send review_rext to preprocess and extract data 

review_text = review_text.apply(preprocess)

# Now sellect how many data entries will be analysed out of all in Data set 
#Included possible error handling 
#first I will get number of data lines in the dataframe
num_of_rows = len(df_subset)

# calling function to get user entry how many data entries to analyze
number=get_number_of_entries(num_of_rows)

entries_to_analyze = review_text.head(number)
row=0  
for text in entries_to_analyze:
    # analyze sentiment using function and append result 
    sentiment_result = get_sentiment(text)
   #Now I will print results and some product data with reviews to evaluate sentiment predictions
    print()
    print('-----------------------------------------------')
    print("Product data  and review text :")
    print()
    print(df_subset.iloc[row])
    row=row+1
    print('-----------------------------------------------')
    print()
    print("polarity score :" ,end=" ")
    print(sentiment_result)
    print("This was a ",end=" ")
    print ("Positive "if sentiment_result>0 else "Negative ","Review")
    

    








