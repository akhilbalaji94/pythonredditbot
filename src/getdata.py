import praw
from sklearn import svm
r = praw.Reddit(user_agent='my_reddit_svm')
submissions = r.get_subreddit('dota2').get_hot(limit=10)
for x in submissions:
	print x
