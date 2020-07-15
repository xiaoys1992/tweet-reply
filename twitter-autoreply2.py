# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 11:31:15 2020

@author: xiaoy
"""

# geektechstuff
# Twitter Application

from twython import Twython
#Twython is a Twitter Python library

import datetime
import time


#imports the Twitter API keys


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# This posts Tweets
# message = "geektechstuff.com Test Tweet aka /'Hello World!/'"
# twitter.update_status(status=message)
# print("Tweeted: %s" % message)

# This searches Tweets

print('GeekTechStuff Twitter Search Python Program')
print('')
search_term = 'Durbin'

username_result = twitter.show_user(screen_name='SenatorDurbin')

tweets_num=username_result['statuses_count']

#id: 247334603

#durbin_tweets= twitter.get_user_timeline(screen_name='SenatorDurbin', count=2)
my_tweets=twitter.get_user_timeline(screen_name='yux415', count=2)

message='@' +'SenatorDurbin'+" "+"That is surprising"

message1='@' +'yux415'+" "+"Hello Yuni"

def get_tids(tweets):
    tids=[]
    for result in tweets:
        tids.append(result['id'])
    return tids
tids=get_tids(my_tweets)

end=time.time()+300

while time.time()<end:
    my_tweets2=twitter.get_user_timeline(screen_name='yux415', count=2)
    new_tids=get_tids(my_tweets2)
    for tid in new_tids:
        if tid<=tids[0]:
            break
        else:
            twitter.update_status(status=message1, in_reply_to_status_id=tid)
    tids=new_tids
    time.sleep(30)

