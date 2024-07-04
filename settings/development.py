from .base import *
import os, socket
from dotenv import load_dotenv
load_dotenv()

ip_address = socket.gethostbyname(socket.gethostname())

DEBUG = True
SECRET_KEY = 'django-insecure-l637sn-6cr-fz(r^bk-lfj-cgxz$(w9@r##!kl*!2&rbd4hor$'

ALLOWED_HOSTS = [ip_address,'127.0.0.1']
CSRF_TRUSTED_ORIGINS = [f"http://{ip_address}","http://127.0.0.1"]

print(f"Connect on this address:") # get the ip address from the command line.
print(f"http://127.0.0.1:8000")
print(f"{ip_address}:8000 \nDocker Container may have different IP, VPN will screw IP address as well\nMight not work on those cases")

database_dict = {
    'sqlite' :  {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        } ,
    'postgres' : {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', "OnlineRetailPOS"),  # Use environment variable DB_NAME, defaulting to 'default_db_name'
            'USER': os.getenv('DB_USERNAME'),  # Use environment variable DB_USERNAME
            'PASSWORD': os.getenv('DB_PASSWORD'),  # Use environment variable DB_PASSWORD
            'HOST': os.getenv('DB_HOST', "localhost"),  # Use environment variable DB_HOST
            'PORT': os.getenv('DB_PORT', ''),  # By default, PostgreSQL uses port 5432
        } ,
    'mysql': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME', "OnlineRetailPOS"),  # Use environment variable DB_NAME
            'USER': os.getenv('DB_USERNAME'),  # Use environment variable DB_USERNAME
            'PASSWORD': os.getenv('DB_PASSWORD'),  # Use environment variable DB_PASSWORD
            'HOST': os.getenv('DB_HOST', "localhost"),  # Use environment variable DB_HOST
            'PORT': os.getenv('DB_PORT', ''),
            'OPTIONS':{
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
    }
}

print(f"Database configuration is set to {database_dict[os.getenv('NAME_OF_DATABASE', 'sqlite')]['ENGINE']}")

DATABASES = {
    'default':  database_dict[os.getenv('NAME_OF_DATABASE', 'sqlite')]

}

# Store Information
# For Line Break add \n
#Can not be more than (RECEIPT_CHAR_COUNT - 2) Characters per line(\n), if wants to add more break it up by \n new line
RECEIPT_CHAR_COUNT = int(os.getenv('RECEIPT_CHAR_COUNT', 32))
STORE_NAME = os.getenv('STORE_NAME', "PJTECH INC")  #Can not be more than RECEIPT_CHAR_COUNT
STORE_ADDRESS = os.getenv('STORE_ADDRESS', "1, Alison Avenue, Lagos.")
STORE_PHONE = os.getenv('STORE_PHONE', "")
RECEIPT_HEAD = f"{STORE_NAME}\n{STORE_ADDRESS}"
RECEIPT_HEAD = RECEIPT_HEAD + f"\n{STORE_PHONE}" if os.getenv('Include_Phone_In_Heading',"False").lower() == "true" else RECEIPT_HEAD
RECEIPT_ADDITIONAL_HEADING = os.getenv('RECEIPT_ADDITIONAL_HEADING', "")
RECEIPT_HEADER = f"{RECEIPT_HEAD}\n{RECEIPT_ADDITIONAL_HEADING}" if RECEIPT_ADDITIONAL_HEADING != "" else RECEIPT_HEAD
RECEIPT_FOOTER = os.getenv('RECEIPT_FOOTER',"Thank You")


# Printer Settings
PRINTER_VENDOR_ID = os.getenv('PRINTER_VENDOR_ID', "")
PRINTER_PRODUCT_ID = os.getenv('PRINTER_PRODUCT_ID', "")
PRINT_RECEIPT = os.getenv('PRINT_RECEIPT', False)
CASH_DRAWER = os.getenv('CASH_DRAWER', False)
