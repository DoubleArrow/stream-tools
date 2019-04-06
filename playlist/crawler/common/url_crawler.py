# -*- coding: utf-8 -*-
# filename: ahnd_url_crawler.py

import ssl
from urllib.request import Request, urlopen

ssl._create_default_https_context = ssl._create_unverified_context


class UrlCrawler(object):

    def __init__(self, parser=None, url_mapper=lambda x: x, debug=False):
        """
        depth: how many time it will bounce from page one (optional)
        cache: a basic cache controller (optional)
        """
        self.url_map = {}
        self.init_url = ''
        self.url_parser = parser
        self.url_mapper = url_mapper
        self.debug = debug

    def crawl(self, url):
        """
        url: where we start crawling, should be a complete URL like
        'http://www.intel.com/news/'
        no_cache: function returning True if the url should be refreshed
        """
        self.init_url = url
        print(" to crawl url:%s" % url)

        html = self.curl(url)

        self.url_parser.parse(html)
        self.url_map = self.url_parser.url_map

        if self.debug or len(self.url_map) == 0:

            if len(self.url_map) == 0:
                print("crawl url:{} return empty".format(url))
            print(html)


    def curl(self, url):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            print("retrieving url... %s" % (url))
            # req = Request('%s://%s%s' % (self.scheme, self.domain, url))
            req = Request(url)

            req.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.i/605.1.15')

            response = urlopen(req, timeout=1)

            # print(response.encoding)

            if response.url != req.full_url:
                return response.url

            charset = self.url_parser.charset

            if response.headers.get_content_charset():
                charset = response.headers.get_content_charset()
            return response.read().decode(charset, 'ignore')
        except Exception as e:
            print("error %s: %s" % (url, e))
            return ''

    @staticmethod
    def curl(url, charsert='utf-8'):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            print("retrieving url... %s" % (url))
            # req = Request('%s://%s%s' % (self.scheme, self.domain, url))
            req = Request(url)

            req.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.i/605.1.15')

            response = urlopen(req, timeout=1)

            # print(response.encoding)

            if response.url != req.full_url:
                return response.url

            if response.headers.get_content_charset():
                charset = response.headers.get_content_charset()
            return response.read().decode(charset, 'ignore')
        except Exception as e:
            print("error %s: %s" % (url, e))
            return ''
