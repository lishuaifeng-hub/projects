import re
import requests
import logging
from core.datasave import DataSave
from bs4 import BeautifulSoup

logger = logging.getLogger("main.scheduler.htmlparse")


class HtmlParse:
    # 主输出方法，返回提取的URL列表与待保存的数据
    def parse_data(self, page_url, data):
        logger.info("开始分析提取数据")
        # 如果待分析的文章的URL或者数据为空，则不做处理
        if page_url is None or data is None:
            return
        soup = BeautifulSoup(data, 'lxml')
        # 分别调用get_urls和get_data()获取数据
        urls = self.get_urls(soup)
        data = self.get_data(page_url, soup)
        return urls, data

    def get_urls(self, soup):
        urls = list()
        #获取文章地址Tag
        links = soup.select('a[href*="/movie/"]')
        for link in links:
            # "从Tag中提取网址数据"
            url = link['href']
            if not url.startswith("https:"):
                urls.append("https:"+url)
            else:
                urls.append(url)
        return urls

    #获取文章数据
    def get_data(self, page_url, soup):
        data = {}
        # 将文章的地址、标题、发布日期保存到字典中
        # 文章URL只是使用参数url
        data['url'] = page_url
        # 获取文章标题
        title = soup.select_one('.cnbeta-article > header > h1')
        # 获取发布日期
        release_date = soup.select_one(".cnbeta-article > header > .meta >span")
        # 将数据保存到一个字典变量中
        data["title"] = title.get_text()
        data["release_date"] = release_date.get_text()
        logger.info("文章url:{}".format(page_url))
        logger.info("数据:{}".format(data))
        return data


if __name__ == "__main__":
    url = 'https://www.cnbeta.com/articles/science/913723.htm'
    save = DataSave("D:\\CodeSpace\\PycharmProjects\\cnBate\\file.txt")
    response = requests.get(url)
    html_data = response.content.decode("utf-8")
    parse = HtmlParse()
    url,  data = parse.parse_data(url, html_data)
    save.save(data)
