
import tweepy
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post


@receiver(post_save, sender=Post)
def tweet_post(sender, instance, **kwargs):
    twitter_auth_keys = {
        "consumer_key": "SVgJVcrNUiLpZ0GdTsYTf0w4K",
        "consumer_secret": "IwBd643m4zrbFDbqJpE86yaDvKvKa3WzE7tupeyL64aMHwxRgl",
        "access_token": "1396845933514665989-AyndQhTLHzyELlwEt1wGfC0BBL48b5",
        "access_token_secret": "81KDxrbEReSBzqp1GfU1qvYbRyGoUqM6TuCvuglm0dTZA"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    tweet = instance.title
    
    try:
        api.update_status(tweet)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            print('duplicate message')