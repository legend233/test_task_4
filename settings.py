from dotenv import load_dotenv
import os

load_dotenv()
db_login = os.getenv("DB_LOGIN")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")