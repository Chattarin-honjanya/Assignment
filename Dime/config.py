## Config File

# API Connection Parameters
API_KEY = 'uuGvJ1enYdZzE1wFMFPvWSz2f28xkRtB'
SYMBOL_LIST_URL = 'https://financialmodelingprep.com/api/v3/stock/list?apikey={API_KEY}'
HISTORICAL_DIVIDEND_URL = 'https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{symbol}?apikey={API_KEY}'
DELISTED_COMPANY_URL = 'https://financialmodelingprep.com/api/v3/delisted-companies?apikey={API_KEY}'

# MySQL Connection Parameters
MYSQL_HOST = 'localhost'  # Replace with your MySQL server host
MYSQL_USER = 'root'       # Replace with your MySQL username
MYSQL_PASSWORD = '<PASSWORD>'  # Replace with your MySQL password
MYSQL_DATABASE = '<DATABASE_NAME>'  # Replace with your MySQL database name

# SQLAlchemy Connection String
CONNECTION_STRING = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}'