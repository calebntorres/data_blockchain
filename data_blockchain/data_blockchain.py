import json
import requests
import pandas as pd
import numpy as np

# processes requests of certain types with a hash 
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
        
    if request_type = == 'm_blocks'
        
    return data

# returns a dataframe of block metadata
def blockMetaData(blk_hash):
    
    sb_data = request('single_block', blk_hash)
    
    block_items = sb_data.items()
    metadata = list(block_items)[:12]
    data = dict(metadata)
    
    tuples = [(k, v) for k, v in data.items()]
    df = pd.DataFrame({x[0]:x[1:] for x in tuples})
    
    return df

# retrurns transaction data for all transactions in a given block
def block_transactions(blk_hash):
    sb_data = request('single_block', blk_hash)
    block_items = sb_data.items()
    raw_transactions = list(block_items)[12:]
    transactions_dict = dict(raw_transactions)

    transactions = transactions_dict['tx']

    tx_df = pd.DataFrame.from_dict(transactions)
    return tx_df