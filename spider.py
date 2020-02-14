from urllib.request import urlopen
from finder import Finder
from scrp import *
# creating a class variables


class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue = ''
    crawled = ''
    queue_set = set()
    crawled_set = set()
    # setting variables to the class

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('first page', Spider.base_url)
    # boot method
    @staticmethod
    def boot(self):
        prj_dir(Spider.project_name)
        dat_files(Spider.project_name, Spider.base_url)
        spider.queue = file_set(Spider.queue_file)
        Spider.crawled = file_set(Spider.crawled_file)

    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) +
                  ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue_set.remove(page_url)
            Spider.crawled_set.add(page_url)
            Spider.update_files()
