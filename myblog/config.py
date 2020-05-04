# _*_encoding:utf-8_*_
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "blog_db"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI  # 创建数据库连接事例
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 动态追踪修改设置，如果未设置只会提示警告
SQLALCHEMY_ECHO = False  # 查询时会显示原生SQL语句
SECRET_KEY = "X1X2X3X4X5X6"


BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
