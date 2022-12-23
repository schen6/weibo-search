# -*- coding: utf-8 -*-
from datetime import date
import datetime
import sys
sys.path.append('/home/panther/')
sys.path.append('/home/panther/weibo-search')
import vagabond.crawlers.PostgresWriter as p
import os
import vagabond.tools.scrapydt as scrapydt
# import importlib
# headers = importlib.import_module("headers")


import configparser
cfp = configparser.ConfigParser()
root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
cfp_path = root_path + '/social.conf'
cfp.read(cfp_path)
#
# st_dt, end_dt = scrapydt.get_dates()
# print(st_dt, end_dt)
#
# print(cfp.get('date', 'crawl_date'))
# #
# if cfp.get('date','crawl_date'):
#     dt = cfp.get('date','crawl_date')
#     t = datetime.datetime.strptime(dt, '%Y-%m-%d')
#     if t.date() < datetime.datetime.now().date():
#         t = t + datetime.timedelta(days=1)
#         new_t = t.strftime("%Y-%m-%d")
#     cfp.set('date', 'crawl_date', new_t)
#     with open(cfp_path, 'w') as configfile:
#         cfp.write(configfile)


client = p.PostgresWriter()
sql = '''
    select cookie from social.weibo_c where comp = 'lenovo'
'''
cookie = client.fetch_data(sql)
client.client.close()
cookie = cookie['cookie'][0]

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 0
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'referer': 'https://weibo.com/',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'cookie': cookie

}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.PGPipeline': 301,
    # 'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = [
    '卡塔尔vs厄瓜多尔',
    '塞内加尔vs荷兰',
    '卡塔尔vs塞内加尔',
    '荷兰vs厄瓜多尔',
    '厄瓜多尔vs塞内加尔',
    '荷兰vs卡塔尔',
    '英格兰vs伊朗',
    '美国vs威尔士',
    '威尔士伊朗',
    '英格vs兰美国',
    '威尔士vs英格兰',
    '伊朗vs美国',
    '阿根廷vs沙特阿拉伯',
    '墨西哥vs波兰',
    '波兰vs沙特阿拉伯',
    '阿根廷vs墨西哥',
    '波兰vs阿根廷',
    '沙特阿拉伯vs墨西哥',
    '丹麦vs突尼斯',
    '法国vs澳大利亚',
    '突尼斯vs澳大利亚',
    '法国vs丹麦',
    '澳大利亚vs丹麦',
    '突尼斯vs法国',
    '德国vs日本',
    '西班牙vs哥斯达黎加',
    '日本vs哥斯达黎加',
    '西班牙vs德国',
    '日本vs西班牙',
    '哥斯达黎加vs德国',
    '摩洛哥vs克罗地亚',
    '比利时vs加拿大',
    '比利时vs摩洛哥',
    '克罗地亚vs加拿大',
    '克罗地亚vs比利时',
    '加拿大vs摩洛哥',
    '瑞士vs喀麦隆',
    '巴西vs塞尔维亚',
    '喀麦隆vs塞尔维亚',
    '巴西vs瑞士',
    '塞尔维亚vs瑞士',
    '喀麦隆vs巴西',
    '乌拉圭vs韩国',
    '葡萄牙vs加纳',
    '韩国vs加纳',
    '葡萄牙vs乌拉圭',
    '加纳vs乌拉圭',
    '荷兰vs美国',
    '阿根廷vs澳大利亚',
    '日本vs克罗地亚',
    '巴西vs韩国',
    '英格兰vs塞内加尔',
    '法国vs波兰',
    '摩洛哥vs西班牙',
    '葡萄牙vs瑞士',
    '荷兰vs阿根廷',
    '克罗地亚vs巴西',
    '英格兰vs法国',
    '摩洛哥vs葡萄牙',
    '阿根廷vs克罗地亚',
    '法国vs摩洛哥',
    '阿根廷vs法国',
    '克罗地亚vs摩洛哥'

]  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2022-11-19'  # '2021-04-17'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2022-12-20'  # '2021-04-18'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 5
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
