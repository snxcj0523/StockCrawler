from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import sys

setting = get_project_settings()
process = CrawlerProcess(setting)
IDD=sys.argv[1]
for spider_name in process.spiders.list():
    print ("Running spider %s" % (spider_name))
    process.crawl(spider_name,ID=IDD) #query dvh is custom argument used in your scrapy

process.start()