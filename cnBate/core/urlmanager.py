import logging
logger = logging.getLogger("main.scheduler.urlmanager")

class URLmanager(object):
    def __init__(self):
        # 初始化带爬取的和已爬取的url的集合
        self.new_urls = set()
        self.old_urls = set()

    def save_new_url(self, url):
        # 将单条的url保存到待爬取的集合中
        if url is not None:
            if url not in self.new_urls and url not in self.old_urls:
                logger.info("保存新URL:{}".format(url))
                self.new_urls.add(url)

    def save_new_urls(self,url_list):
        # 批量存储URL
        for url in url_list:
            self.save_new_url(url)

    def get_new_url(self):
        # 取出一条未爬取的URL，同时保存到已爬取的URL中
        if self.get_new_url_num() > 0:
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def get_new_url_num(self):
        # 返回未爬取的url的数量
        return len(self.new_urls)

    def get_old_url_num(self):
        # 返回已经爬取的URL数量
        return len(self.old_urls)