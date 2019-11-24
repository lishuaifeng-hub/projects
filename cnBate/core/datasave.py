import os
import logging
logger = logging.getLogger("main.scheduler.datasave")

class DataSave:
    def __init__(self, path):
        self.path = path

    def save(self, data):
        # 判断文件路径是否存在，若不存在，则抛出错误
        if not os.path.exists(self.path):
            logger.error("文件路径不存在")
            raise FileExistsError("文件路径不存在")
        # 将数据写入文件中，以追加的形式写入文件
        with open(self.path, 'a', encoding="utf-8") as fp:
            logger.info("开始写入数据")
            fp.write(str(data) + '\n')


if __name__ == "__main__":
    test_data = "this is a test,\n save it"
    save_path = 'D:\\CodeSpace\\PycharmProjects\\cnBate\\file.txt'
    ds = DataSave(save_path)
    ds.save(test_data)