## Questionnaire to use with tweet_collection.py
from questionnaire import Questionnaire

def Questions():
  '''
  AIM -> Create a good looking questionnaire to generate required arguments to be used with tweet_collection
  OUTPUT -> String with desired arguments
  '''

  # Initialize Questionnaire
  q = Questionnaire()

  # Create Raw Questions
  q.raw('Search Keyword')
  q.raw('Number of Tweets', type=int)
  q.raw('CSV Name')

  # Run the module
  q.run()

  return q.format_answers()