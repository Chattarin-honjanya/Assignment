import config_dime as cf
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

WRITE_MODE_REPLACE = 'replace'
HISTORICAL_DIVIDEND = 'historical'

# Get config
api_key = cf.API_KEY
symbol_url = cf.SYMBOL_LIST_URL.format(API_KEY=api_key)
delisted_url = cf.DELISTED_COMPANY_URL.format(API_KEY=api_key)
connection_string = cf.CONNECTION_STRING.format(user=cf.MYSQL_USER,password=cf.MYSQL_PASSWORD,host=cf.MYSQL_HOST,database=cf.MYSQL_DATABASE)

def get_data(url):
    """Make a GET request to the API and return the parsed JSON data."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def get_symbol_df():
    """Get DataFrame of symbols."""
    json_result = get_data(symbol_url)
    return pd.DataFrame(json_result) if json_result else pd.DataFrame()

def get_dividends_historical_df(symbol):
    """Get DataFrame of historical dividends for a symbol."""
    dividends_historical_url = cf.HISTORICAL_DIVIDEND_URL.format(symbol=symbol, API_KEY=api_key)
    json_result = get_data(dividends_historical_url)
    """ Use json_normalize to extract values from the JSON column """
    result_df = pd.json_normalize(json_result[HISTORICAL_DIVIDEND])
    result_df['symbol'] = json_result['symbol']
    result_df = result_df[['symbol'] + [col for col in result_df.columns if col != 'symbol']]
    return result_df

def get_delisted_company_df():
    """Get DataFrame of delisted companies."""
    json_result = get_data(delisted_url)
    return pd.DataFrame(json_result) if json_result else pd.DataFrame()

def start_engine(connection_string):
    """Start the SQLAlchemy engine."""
    return create_engine(connection_string)

def close_engine(engine):
    engine.dispose()

def retrive_data(table_name,datebase_name=cf.MYSQL_DATABASE):
    engine = start_engine(connection_string)

    query = f"SELECT * FROM {datebase_name}.{table_name}"  # Replace with your table name
    
    # Read data into a pandas DataFrame using the engine
    result_df = pd.read_sql(query, engine)

    # # Close the SQLAlchemy engine
    close_engine(engine)

    return result_df

def write_data(df,table_name,write_mode = 'replace'):
    engine = start_engine(connection_string)
    created_at = datetime.now()
    df['created_at'] = created_at
    # Save DataFrame to MySQL table
    result_status = df.to_sql(name=table_name, con=engine, index=True, if_exists= write_mode)

    # # Close the SQLAlchemy engine
    close_engine(engine)

    return result_status