from dotenv import load_dotenv
import os

load_dotenv()
db_login = os.getenv("DB_LOGIN")
db_password = os.getenv("DB_PASSWORD")