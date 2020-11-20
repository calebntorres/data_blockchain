import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime

# processes api requests single blocks, single transcations and blockheights with a hash 
def request(request_type, parameter):
    
    if request_type == 'single_block':
        block_hash = parameter
        sb_base = f'https://blockchain.info/rawblock/{block_hash}'
        url = sb_base
        request = requests.get(url)
        data = request.json()
        
    if request_type == 'single_tx':
        tx_hash = parameter
        st_base = f'https://blockchain.info/rawtx/{tx_hash}'
        url = st_base
        request = requests.get(url)
        data = request.json()
        
    if request_type == 'block_ht':
        block_ht = parameter
        block_ht_base = f'https://blockchain.info/block-height/{block_ht}?format=json'
        url = block_ht_base
        request = requests.get(url)
        data = request.json() 
        
    #if request_type  == 'm_blocks':

        
    return data

# returns a dataframe of a single block's metadata
def blockMetaData(blk_hash):
    
    sb_data = request('single_block', blk_hash)
    
    block_items = sb_data.items()
    metadata = list(block_items)[:12]
    data = dict(metadata)
    
    tuples = [(k, v) for k, v in data.items()]
    df = pd.DataFrame({x[0]:x[1:] for x in tuples})
    
    return df

# retrurns transaction data for all transactions in a given block via dataframe
def block_transactions(blk_hash):
    sb_data = request('single_block', blk_hash)
    block_items = sb_data.items()
    raw_transactions = list(block_items)[12:]
    transactions_dict = dict(raw_transactions)

    transactions = transactions_dict['tx']

    tx_df = pd.DataFrame.from_dict(transactions)
    return tx_df

# returns hash of the latest block on the blockchain
def latestBlockHash():
    url = 'https://blockchain.info/latestblock'
    request = requests.get(url)
    data = request.json()
    
    blk_hash = data['hash']
    
    return blk_hash

# returns unix timestamp of current time
def currentTime():
    unix_time = int(round(time.time()))*1000
    
    return unix_time

# returns unix timestamp of specified time with string format "dd/mm/yyy"
def getTime(time_string):
    epoch_time = time.mktime(datetime.datetime.strptime(time_string, "%d/%m/%Y").timetuple())
    unix_time = epoch_time*1000
    
    return unix_time

def getBlocks():
    time = getCurrentTime
    
 # returns json request of latest block in blockchain   
def getLatestBlock():
    blk_hash = latestBlockHash()
    block = request('single_block', blk_hash)
    
    return block
