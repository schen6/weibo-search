#!/bin/sh
cd /home/panther
. ./venv/bin/activate
cd weibo-search
#scrapy crawl search
SCRAPY_PROJECT=chando scrapy crawl search
SCRAPY_PROJECT=clarins scrapy crawl search
