class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://user:wanjagi87@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"
    JWT_SECRET_KEY = "your_jwt_secret_key"
    