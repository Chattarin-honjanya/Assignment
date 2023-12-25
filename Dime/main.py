import common_function as cmmn_fc

# Constants
SYMBOL_TABLE = 'symbol'
DIVIDENDS_HIST_TABLE = 'dividends_hist'
DELISTED_COMPANY_TABLE = 'delisted_company'

# Get Symbol
symbol_df = cmmn_fc.get_symbol_df()
symbol_write_status = cmmn_fc.write_data(df=symbol_df, table_name=SYMBOL_TABLE)
print("Symbol Write Status:", symbol_write_status)

symbol_read_df = cmmn_fc.retrive_data(table_name=SYMBOL_TABLE)
print("Symbol Read Data:")
print(symbol_read_df.head())

# Get Dividend Historical
symbol = 'AAPL'
dividends_historical_df = cmmn_fc.get_dividends_historical_df(symbol)
dividends_hist_write_status = cmmn_fc.write_data(df=dividends_historical_df, table_name=DIVIDENDS_HIST_TABLE)
print("Dividends Historical Write Status:", dividends_hist_write_status)

dividends_hist_read_df = cmmn_fc.retrive_data(table_name=DIVIDENDS_HIST_TABLE)
print("Dividends Historical Read Data:")
print(dividends_hist_read_df.head())

# Get Delisted Companies
delisted_company_df = cmmn_fc.get_delisted_company_df()
delisted_company_write_status = cmmn_fc.write_data(df=delisted_company_df, table_name=DELISTED_COMPANY_TABLE)
print("Delisted Company Write Status:", delisted_company_write_status)

delisted_company_read_df = cmmn_fc.retrive_data(table_name=DELISTED_COMPANY_TABLE)
print("Delisted Company Read Data:")
print(delisted_company_read_df.head())


