import praw, re, urllib, datetime


def setup():
    r = praw.Reddit('reddit_dev', user_agent='osmc:earthporn-scraper:v0.5 (by /u/k0nsi)')
    return r


def get_subs(subs, limit, r):
    submissions = list()

    for sub in subs:
        subr = r.subreddit(sub)
        links = subr.hot(limit=limit)
        submissions.extend(links)
    return submissions


def download_subs(subs, location):
    loop = 0
    regexp = re.compile('((https:\/\/i\.)|(\.jpg)$|imgur)')
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
                size = urllib.urlopen(url).info()['Content-Length']
                print('Size is ' + size)
                if int(size) < 10000000:
                    urllib.urlretrieve(url, location + filename)
            except Exception, e:
                print(str(e))


def valid_image_name(filename):
    regexp = re.compile(r'(jpg)$')
    if regexp.search(filename) is None:
        return filename + '.jpg'
    else:
        return filename


def fix_imgur_link(link):
    return link.replace('imgur', 'i.imgur', 1) + '.jpg'


def main():
    subs = ['earthporn', 'villageporn', 'houseporn']
    print('==================================')
    print('Start time: ' + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    print("Starting call...")
    r = setup()
    links = get_subs(subs, 8, r)
    download_subs(links, '/home/osmc/Pictures/Alle_Fotos/')
    print('Finished at ' + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    print('==================================')
    print('\n')


if __name__ == '__main__':
    main()
