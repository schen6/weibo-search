#!/bin/sh
cd /home/panther
. ./venv/bin/activate
cd weibo-search
#scrapy crawl search
SCRAPY_PROJECT=eyedrops scrapy crawl search



