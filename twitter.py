import tweepy
import csv
import sys
import datetime
import ast
import oauth_info as authkeys 

def Tweet_collection(data):

  '''
  AIM -> Collect X amount of desired tweets based on inputted search term
  INPUT ->  Search Keyword, Defined CSV file to create, Number of tweets
  OUTPUT -> CSV file with raw extracted tweets based on search term
  '''

  # Variables
  data_dict = ast.literal_eval(data) # Transform string to dict type
  search_keyword = data_dict['Search Keyword']
  num_tweets = data_dict['Number of Tweets']
  csv_name = data_dict['CSV Name']

  # Twitter Auth
  auth = tweepy.OAuthHandler(authkeys.CONSUMER_KEY, authkeys.CONSUMER_SECRET)
  auth.set_access_token(authkeys.ACCESS_TOKEN, authkeys.ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)

  # Open CSV file that you want to write in
  open_csv_write = open('{}.csv'.format(csv_name), 'w')

  # Initialize the csv writer
  field_names = ['Created At', 'Tweet']
  csv_writer = csv.DictWriter(open_csv_write, field_names)

  # Create the header for CSV file
  csv_writer.writeheader()

  #Writes the tweets into a csv file
  for tweet in tweepy.Cursor(api.search,q=search_keyword+' -filter:retweets', lang='en').items(num_tweets):
    csv_writer.writerow({'Created At': datetime.date.today(), 'Tweet': tweet.text})

  open_csv_write.close()

  pass 