#!/bin/sh
cd /home/panther
. ./venv/bin/activate
cd weibo-search
#scrapy crawl search
SCRAPY_PROJECT=mamonde scrapy crawl search
