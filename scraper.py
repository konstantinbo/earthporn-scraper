#!/usr/bin/env python3

import praw, re, urllib


def setup(user_agent):
    r = praw.Reddit(user_agent=user_agent)
    return r


def get_subs(name, limit, r):
    submissions = r.get_subreddit(name).get_hot(limit=limit)
    return submissions


def download_subs(subs):
    loop = 0
    regexp = re.compile(r'((https://i\.)|(\.jpg)$)')
    for x in subs:
        loop += 1
        print(loop)
        print(x.url)
        if regexp.search(x.url) is not None:
            urllib.request.urlretrieve(x.url, './pic' + str(loop) + '.jpg')


def main():
    print("Starting call...")
    r = setup('elementary-os:earthporn-scraper:v0.2 (by /u/k0nsi)')
    subs = get_subs('earthporn', 5, r)
    download_subs(subs)

if __name__ == '__main__':
    main()


