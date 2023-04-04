import os
from dotenv import load_dotenv
from pathlib import Path

from MySQLdb import _mysql


dotenv_path = Path('./config/prod.env')
load_dotenv(dotenv_path=dotenv_path)


HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SSL_CERT = os.getenv("SSL_CERT")


def get_connection():

  return _mysql.connect(
          host= HOST,
          user= USERNAME,
          password= PASSWORD,
          database= DATABASE,
          ssl      = {
            "ca": SSL_CERT
          }
        )

connection = get_connection()


# cursor = connection.cursor()