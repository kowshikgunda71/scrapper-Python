import threading
from queue import Queue

from spider import Spider
from dom import *
from scrp import *
from finder import *

PROJECT_NAME = ''
HOMEPAGE = ''
DOMAIN_NAME = get_dom(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue= Queue()  
Spider(PROJECT_NAME, HOMEPAGE,DOMAIN_NAME)

#create spiders 
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name, url)
        queue.task_done()


#seperate queues
def create_jobs():
    for link in file_set(QUEUE_FILE):
        queue.put(list)
    queue.join()
    crawl()



#check if items in queue and crawl 
def crawl():
    queued_link= file_set(QUEUE_FILE)
    if len( queued_link) >0:
        print(str(len(queued_link))+ 'still left')
        create_jobs()


