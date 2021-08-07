#!/bin/sh
cd /home/panther
. ./venv/bin/activate
cd weibo-search
#scrapy crawl search
#SCRAPY_PROJECT=adolph_h scrapy crawl search
#SCRAPY_PROJECT=kerastase_h scrapy crawl search
#SCRAPY_PROJECT=kono_h scrapy crawl search
#SCRAPY_PROJECT=lorealhair_h scrapy crawl search
#SCRAPY_PROJECT=renefurterer_h scrapy crawl search
#SCRAPY_PROJECT=ryo_h scrapy crawl search
#SCRAPY_PROJECT=schwarzkopf_h scrapy crawl search
#SCRAPY_PROJECT=seeyoung_h scrapy crawl search
#SCRAPY_PROJECT=triptych_h scrapy crawl search

SCRAPY_PROJECT=bodyaid_h scrapy crawl search
SCRAPY_PROJECT=hairrecipe_h scrapy crawl search
