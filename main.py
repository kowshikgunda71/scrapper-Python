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



