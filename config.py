class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/event_scheduler"  # No password
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "53d1766d591eea31c5309e008d1f37d3a831ccf68e98889da8f67d44150a5951"