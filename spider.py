from urllib.request import urlopen
from finder import Finder
from scrp import *
class Spider:
    project_name = ''
    base_url=''
    domain_name=''
    queue=''
    crawled=''
    queue_set= set()
    crawled_set=set()
    def __init__(self,project_name, base_url, domain_name):
        Spider.project_name=project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue=Spider.project_name + '/queue.txt'
        Spider.crawled=Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('first page', Spider.base_url)
    
    def boot(self):
        prj_dir(Spider.project_name)
        dat_files(Spider.project_name, Spider.base_url)

   
