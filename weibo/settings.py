# -*- coding: utf-8 -*-
from datetime import date
import datetime

today = date.today()
yesterday = today + datetime.timedelta(days=-1)

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 2
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': 'login_sid_t=5eefddc179e3277c9fedfe8e4685309f; cross_origin_proto=SSL; WBStorage=8daec78e6a891122|undefined; _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=7644084570556.38.1618737251515; SINAGLOBAL=7644084570556.38.1618737251515; ULV=1618737251521:1:1:1:7644084570556.38.1618737251515:; wb_view_log_2951321360=1920*10801; SUB=_2A25Nf4iUDeRhGeRH7lMS8i_PzTyIHXVuDP1crDV8PUNbmtAKLW6hkW9NTcB1ln9-oCEAk0uqzA6-V_6FpIc2LX6i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWWKZWT5uMYkdzZ988zG-YY5JpX5KzhUgL.Foz4SK20eo20So52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoM41h2NeoqceKz0; ALF=1650273348; SSOLoginState=1618737348; wvr=6; webim_unReadCount=%7B%22time%22%3A1618737534101%2C%22dm_pub_total%22%3A16%2C%22chat_group_client%22%3A999%2C%22chat_group_notice%22%3A1%2C%22allcountNum%22%3A1028%2C%22msgbox%22%3A0%7D'
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['欧莱雅']  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 0
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = yesterday  # '2021-04-17'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = yesterday  # '2021-04-18'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
# MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'
