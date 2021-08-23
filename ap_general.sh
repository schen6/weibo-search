#!/bin/sh
cd /home/panther
. ./venv/bin/activate
cd weibo-search
#scrapy crawl search

SCRAPY_PROJECT=general_anti_aging scrapy crawl search
SCRAPY_PROJECT=general_blush scrapy crawl search
SCRAPY_PROJECT=general_eyebrow scrapy crawl search
SCRAPY_PROJECT=general_foundation scrapy crawl search
SCRAPY_PROJECT=general_facial_care scrapy crawl search
SCRAPY_PROJECT=general_facial_care2 scrapy crawl search
SCRAPY_PROJECT=general_hair scrapy crawl search
SCRAPY_PROJECT=general_hufa scrapy crawl search
SCRAPY_PROJECT=general_hufu scrapy crawl search
SCRAPY_PROJECT=general_jinghua scrapy crawl search
SCRAPY_PROJECT=general_lip_other scrapy crawl search
SCRAPY_PROJECT=general_lipstick scrapy crawl search
SCRAPY_PROJECT=general_makeup scrapy crawl search
SCRAPY_PROJECT=general_meibai scrapy crawl search
SCRAPY_PROJECT=general_mianmo scrapy crawl search
SCRAPY_PROJECT=general_toupi scrapy crawl search


