import requests
import datetime
import pytz

import base64
import os
from google.cloud import bigquery

class Config:
    dataset_id = os.environ.get("dataset_id")
    table_name = os.environ.get("table_name")

def get_last_price(symbol) :
    host = 'https://api.bitkub.com'
    path = '/api/market/ticker'
    x = symbol.split('_')
    adj_sym = x[1].upper() + '_' + x[0].upper()  #turn 'doge_thb' to 'THB_DOGE'
    return requests.request('GET', host + path).json()[adj_sym]['last']
  
def get_highestBid_price(symbol) :
    host = 'https://api.bitkub.com'
    path = '/api/market/ticker'
    x = symbol.split('_')
    adj_sym = x[1].upper() + '_' + x[0].upper()
    return requests.request('GET', host + path).json()[adj_sym]['highestBid']
  
def get_lowestAsk_price(symbol) :
    host = 'https://api.bitkub.com'
    path = '/api/market/ticker'
    x = symbol.split('_')
    adj_sym = x[1].upper() + '_' + x[0].upper()
    return requests.request('GET', host + path).json()[adj_sym]['lowestAsk']
  
def servertime():
    host = 'https://api.bitkub.com'
    path = '/api/v3/servertime'
    return requests.request('GET', host + path).text

def get_iso_8601_time():
    unix_timestamp_ms = int(servertime())
    unix_timestamp = unix_timestamp_ms / 1000   # Convert Unix timestamp from milliseconds to seconds
    date_time = datetime.datetime.utcfromtimestamp(unix_timestamp).replace(tzinfo=pytz.utc)  # Convert Unix timestamp to a datetime object in UTC
    iso_8601_format = date_time.isoformat()  # Convert the datetime object to ISO 8601 format with timezone offset
    return iso_8601_format

def insert_data(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict): The dictionary with data specific to this type of event.
         context (google.cloud.functions.Context): The Cloud Functions event metadata.
    """
    client = bigquery.Client()
    dataset_ref = client.dataset(Config.dataset_id)

    symbol = 'doge_thb'
    record= [(get_iso_8601_time() ,
          get_lowestAsk_price(symbol) , 
          get_last_price(symbol),
          get_highestBid_price(symbol))]
    
    table_ref = dataset_ref.table(Config.table_name)
    table = client.get_table(table_ref)
    result = client.insert_rows(table, record)
    return result
  
