import pandas as pd
import nltk
import spacy
import re
import string
import isodate
import ast
import langid
import numpy as np

from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

nltk.download('punkt')

######################################################## 1_Extracting Data ##########################################################################


def get_channel_info(youtube, channel_idx):
    lst = []

    request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=','.join(channel_idx)
    )
    response = request.execute()
    for i in response['items']:
        data = {'Channel_Name': i['snippet']['title'],
                'Published_at': i['snippet']['publishedAt'],
                'No_of_subscribers': i['statistics']['subscriberCount'],
                'No_of_views': i['statistics']['viewCount'],
                'Total_Videos':i['statistics']['videoCount'],
                'Playlist_Id': i['contentDetails']['relatedPlaylists']['uploads']  
        }
    lst.append(data)
    df = pd.DataFrame(lst)
        

    return df

def get_channel_idx(youtube, playlist_id):
    
    video_idx = []

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults = 50
    )
    response = request.execute()

    for item in response['items']:
        video_idx.append(item['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50,
                    pageToken = next_page_token)
        response = request.execute()

        for item in response['items']:
            video_idx.append(item['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')

    return video_idx

def all_video_details(youtube, video_idx):
    lst = []
    
    for i in range (0, len(video_idx), 50):
        request = youtube.videos().list(
            part = 'snippet, contentDetails, statistics',
            id = ','.join(video_idx[i:i+50])
        )
        response = request.execute()
        for video in response['items']:
            info = {'snippet':['channelTitle', 'title', 'description', 'publishedAt', 'tags'],
                             'statistics':['viewCount','likeCount', 'commentCount'],
                             'contentDetails': ['duration']
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in info.keys():
                for v in info[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            lst.append(video_info)
    df = pd.DataFrame(lst)
    return df

def extract_comments(youtube, video_ids, max_comments_per_video=1000):
    all_comments = []

    for video_id in video_ids:
        try:
            comments_in_video = []
            nextPageToken = None

            while len(comments_in_video) < max_comments_per_video:
                # Request comments with the current nextPageToken
                request = youtube.commentThreads().list(
                    part="snippet,replies",
                    videoId=video_id,
                    maxResults=100,
                    pageToken=nextPageToken
                )
                response = request.execute()

                # Extract comments from the current page
                comments_in_video.extend([comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items']])

                # Check if there are more pages
                nextPageToken = response.get('nextPageToken')
                if not nextPageToken:
                    break

            # Trim the list to the desired max_comments_per_video
            comments_in_video = comments_in_video[:max_comments_per_video]

            comments_in_video_info = {'video_id': video_id, 'comments': comments_in_video}
            all_comments.append(comments_in_video_info)

        except HttpError as e:
            # Handle HTTP errors
            logging.error(f"HTTP error while fetching comments for video {video_id}: {e}")
        except Exception as e:
            # Catch any other exceptions
            logging.error(f"Error while fetching comments for video {video_id}: {e}")

    return pd.DataFrame(all_comments)

################################################### 2_Data Wrangling ###########################################################################

def convert_title(x):
    
    x = x.replace(',', '').lower()
    # Tokenize the text
    word_tokens = word_tokenize(x)

    # Combine '$' with the following number
    combined_tokens = []
    i = 0
    while i < len(word_tokens):
        if word_tokens[i] == '$':
            if i + 1 < len(word_tokens):
                combined_tokens.append(word_tokens[i] + word_tokens[i + 1])
                i += 1  # Skip the next element as it has been combined with '$'
            else:
                combined_tokens.append(word_tokens[i])
        else:
            combined_tokens.append(word_tokens[i])
        i += 1

    # Replace tokens starting with '$' with 'money'
    modified_tokens = ['money' if token.startswith('$') else token for token in combined_tokens]

    # Replace any number with 'number'
    final_tokens = ['number' if token.isdigit() else token for token in modified_tokens]

    # Join the tokens back into a string
    modified_text = ' '.join(final_tokens)
    return modified_text

def tokenize(x):
    custom_stopwords = {'would', '(', ')', '-', ',',  "'s", "’", '40000000th', '001','100000000th','10000000th',
                        '100k','100th','1080p','118','11k','18th','1k','001', '118', '1st', '24k', '30', '3000000th', '3k', '40', '4000000th', '4k', '30', '40', '50', '5000000th', '50k', '6000000th', '7k',
       '8000000th','8byte', '9k'}
    stop_words = set(stopwords.words('english')) | custom_stopwords

    x = re.sub(r'\[a-zA-Z]', ' ', x)
    word_tokens = word_tokenize(x)
    #filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    
    filtered_sentence = []
 
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def preprocess_text(tokens):
    # Lowercase the words
    tokens_lower = [word.lower() for word in tokens]
    
    # Remove punctuation and empty strings
    tokens_no_punct = [''.join(char for char in word if char not in string.punctuation) for word in tokens_lower if word]

    return tokens_no_punct

def lemmatize_tokens(tokens):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]


def days(x):
    date = datetime.fromisoformat(x[:-1])
    day = date.strftime('%A')
    return day

def duration2second(x):
    duration = isodate.parse_duration(x)
    time_delta = pd.to_timedelta(duration)
    seconds = time_delta.total_seconds()
    return seconds

def clean_data(x):
    # Remove non-english char 
    pattern = re.compile(r'[\x00-\x7F!#$%^&*()\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF]')
    filtered_text = ''.join(pattern.findall(x))    
    filtered_text = ast.literal_eval(filtered_text)
    return filtered_text

def remove_blank(x):
    #filtered_text = ast.literal_eval(x)
    filtered_list = [item.strip() for item in x if item.strip()]
    no_whitespace_list = [string.replace("  ", "") for string in filtered_list]
    return no_whitespace_list

def remove_non_english(sentence):
    if isinstance(sentence, str):
        lang, _ = langid.classify(sentence)

        # Function to check if a character is an emoji
       
        # Remove non-English words while keeping emojis
        cleaned_string = ''.join(char if lang == 'en' else ' ' for char in sentence)

        return cleaned_string.strip()
    else:
        return ''
    
def average_sentiments(sentiments, sentiment_type):
    if sentiments:
        return sum(entry[sentiment_type] for entry in sentiments) / len(sentiments)
    
    else:
        return 0.0
    
###################################################################### 3_EDA ###############################################################################
    
def mapping(x):
    if x >= 6000:
        return '> 100 Min'
    if 1200 <= x < 6000:
        return '20 - 100 Min'
    if 600 <= x < 1200:
        return '10 - 20 Min'
    if 300 <= x < 600:
        return '5 - 10 Min'
    if 60 <= x < 300:
        return '1 - 5 Min'
    else:
        return '< 1 Min'
    
def only_words(x):
    
    custom_stopwords = {'would', '(', ')', '-', ',',  "'s", "’", '40000000th', '001','100000000th','10000000th',
                        '100k','100th','1080p','118','11k','18th','1k','001', '118', '1st', '24k', '30', '3000000th', '3k', '40', '4000000th', '4k', '30', '40', '50', '5000000th', '50k', '6000000th', '7k',
                       '8000000th','8byte', '9k',  'youtube', 'youtuber', '001', '118', '30','40','50'}
    
    stop_words = set(stopwords.words('english')) | custom_stopwords

    # Remove variations, punctuation, and convert to lowercase
    x = re.sub(r'[^\w\s]', '', x)
    
    # Tokenize the text
    word_tokens = word_tokenize(x)
    
    # Filter out stopwords
    filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words]
    
    return filtered_sentence

