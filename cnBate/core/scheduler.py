import logging
from core.datasave import DataSave
from core.htmldownloader import HtmlDownloader
from core.htmlparse import HtmlParse
from core.urlmanager import URLmanager
logger = logging.getLogger("main.scheduler")

class Scheduler:
    def __init__(self, path, root_url, count):
        # 初始化各个组件
        self.url_manager = URLmanager()
        self.data_save = DataSave(path)
        self.html_parse = HtmlParse()
        self.downloader = HtmlDownloader()
        self.root_url = root_url
        self.count = count

    def run_spider(self):
        # 先添加一条URL到未爬取URL集合中
        self.url_manager.save_new_url(self.root_url)
        # 判断：如果未爬取URL集合中还有网址，并且还没有爬取到50篇文章，那么继续爬取
        while self.url_manager.get_new_url_num() and self.url_manager.get_old_url_num() < self.count:
            try:
                # 获取一条未爬取URL
                url = self.url_manager.get_new_url()
                # 下载数据
                response = self.downloader.download(url)
                # 分析数据，返回URL与文章相关的数据
                new_urls, data = self.html_parse.parse_data(url, response)
                # 将获取到的URL保存到未爬取的URL集合中
                self.url_manager.save_new_urls(new_urls)
                # 保存数据到本地文件
                self.data_save.save(data)
                logger.info("已经抓取{0}篇文章".format(len(self.url_manager.old_urls)))
            except Exception as e:
                logger.error("本篇文章抓取停止，{0}".format(e))
