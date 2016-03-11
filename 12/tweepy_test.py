import tweepy
import datetime

consumer_key = "lARedxYZ5ZZAyKMmUI5TLLouD"
consumer_secret = "eTwR61RkQmC3VmFeAEwwrpo6DoWt89RiBmzDRxf4P9zQj9106i"
                    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
access_token = "2943937266-ReHfTt05mJzIzATjtBBPbiXCz6MG6tN6USnLaia"
access_token_secret = "4K9tlpNck4pQagPSPLeCbuC5vIkoajKCwLuK4jfYjHK7F"   

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# 트윗 포스트하기   
tweet = str(datetime.datetime.now()) + ' Brain Python Test.'
api.update_status(status=tweet)

print("Successfully Posted.")
print() # 빈 줄 출력

# 타임 라인 읽어오기
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)