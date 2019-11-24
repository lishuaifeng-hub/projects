from core.scheduler import Scheduler
from common.logger_help import Logger
logger = Logger(logger_name="main").get_logger()


if __name__ == "__main__":
    logger.info("==========================start===========================")
    root_url = "https://hot.cnbeta.com/articles/movie/914069.htm"
    save_url = "D:\\CodeSpace\\PycharmProjects\\cnBate\\file.txt"
    Spider = Scheduler(save_url, root_url, 50)
    Spider.run_spider()
    logger.info("==========================end===========================")