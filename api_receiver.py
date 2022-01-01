import requests
from yahoo_fin import stock_info  as si

def get_stock_market_data():
    """
    used for listing the active papers on nasdaq .
    :return: list_nasdaq
    """
    list_nasdaq = si.tickers_nasdaq()
    return list_nasdaq



