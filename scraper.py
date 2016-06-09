import praw
import urllib
r = praw.Reddit(user_agent='elementary-os:earthporn-scraper:v0.1 (by /u/k0nsi)')
submissions = r.get_subreddit('earthporn').get_hot(limit=5)

#print([str(x) for x in submissions])
for x in submissions:
    print(x.url)

#downloads the image from the given url to the current directory
urllib.request.urlretrieve("http://farm8.staticflickr.com//7465//27439812671_2917b68c09_k.jpg", "./pic.jpg");



