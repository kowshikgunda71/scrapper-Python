from urllib.parse import urlparse


def get_dom(url):
    try:
        res = get_sub_dom(url).split('.')
        return res[-2] + '.' + res[-1]
    except:
        return ''


def get_sub_dom(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
