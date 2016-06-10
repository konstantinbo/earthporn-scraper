#!/usr/bin/env python3

import praw, re, urllib


def setup(user_agent):
    r = praw.Reddit(user_agent=user_agent)
    return r


def get_subs(name, limit, r):
    submissions = r.get_subreddit(name).get_hot(limit=limit)
    return submissions


def download_subs(subs, location):
    loop = 0
    regexp = re.compile(r'((https://i\.)|(\.jpg)$|imgur)')
    for x in subs:
        loop += 1
        url = x.url
        print(loop)
        print(url)
        if regexp.search(url) is not None:
            if 'imgur' in url:
                url = fix_imgur_link(url)
            filename = url.split('/')[-1]
            filename = valid_image_name(filename)
            try:
                urllib.request.urlretrieve(url, location + filename)
            except:
                print('Error')


def valid_image_name(filename):
    regexp = re.compile(r'(jpg)$')
    if regexp.search(filename) is None:
        return filename + '.jpg'
    else:
        return filename


def fix_imgur_link(link):
    return link.replace('imgur', 'i.imgur', 1) + '.jpg'


def main():
    print("Starting call...")
    r = setup('elementary-os:earthporn-scraper:v0.2 (by /u/k0nsi)')
    subs = get_subs('earthporn', 8, r)
    download_subs(subs, './')


if __name__ == '__main__':
    main()


