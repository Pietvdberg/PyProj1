import threading
from queue import Queue
from spider import Spider
from domain import *
from shared_functions import *

PROJECT_NAME = 'gebouw-t'
HOMEPAGE = 'https://gebouw-t.nl/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Create worker threads (will die when main exits)
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#Do the next job in the queue
def work():
    while True:
        url = thread_queue.get()
        print("file updated")
        Spider.crawl_page(threading.current_thread().name, url)
        thread_queue.task_done()

#Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()


#Check for items in queue, if so, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links)) + ' links in queue...')
        create_jobs()


create_spiders()
crawl()