import requests
import logging
logger = logging.getLogger("main.scheduler.htmldownloader")

class HtmlDownloader:
    def download(self, url):
        if url is None:
            return None
        else:
            logger.info("开始下载数据，网址{}".format(url))
            response = requests.get(url)
            # 如果请求成功，则返回网页数据，否则返回None
            if response.status_code == 200:
                logger.info("下载数据成功")
                return response.content.decode("utf-8")
            else:
                return None


if __name__ == "__main__":
    url = "http://www.bing.com"
    html_downer = HtmlDownloader()
    bing_html = html_downer.download(url)
    print(bing_html)
