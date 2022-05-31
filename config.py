import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True

# SMTP DATA
MAIL_USERNAME = "cfs.message.send@gmail.com"
MAIL_PASSWORD = "CFSmessage12$"
MAIL_USE_SSL = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
DB = 'db.sl3'
