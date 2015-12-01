import re
import json
import urllib
import tweepy
from hidden import *
from ete2 import Tree,TreeStyle

friends_url = 'https://api.twitter.com/1.1/friends/list.json'
followers_url = 'https://api.twitter.com/1.1/followers/list.json'

def getTwitterAccountName(user):
	return str(re.findall(r", screen_name=u(.+), u",str(user.lists))[0])



#Recursive function
#It can't be executed due to Twitter http request restriction

# def getFriends(user,ref,radius):
# 	print radius
# 	for friend in user.friends():
# 		child = ref.add_child(name=getTwitterAccountName(friend))
# 		getFriends(friend,child,radius)

def getFriends(user,ref,radius):
	for friend in user.friends():
		child = ref.add_child(name=getTwitterAccountName(friend))

def main():

	t = Tree()

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(token_key, secret_key)

	api = tweepy.API(auth)

	root = t.add_child(name=api.me().name)

	for friend in api.me().friends():
		child = root.add_child(name=getTwitterAccountName(friend))
		getFriends(friend,child,0)
	
	#getFriends(api.me(),root,0)

	t.render("mytree.png", w=183, units="mm")


main()

