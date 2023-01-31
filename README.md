# zksync_api
How to get transactions data on the ZKsync mainnet for Open Data Community Hackathon

The Open Data Community participants that are mostly come from Data Science background, so it is very possible that they do not know how to get data from blockchains like ethereum, zksync etc. and it will be time consuming work to understand it. So I decided to prepare an end to end guide with source code to explain how to get data from ZKsync blockchain that even maybe be a little harder to work with it, and by this tutorial make this procedure easier for them.

## Methodology : 
There are multiple ways to get data of transactions from ZKsync but the best simple one and fast one is using ZKsync official APIs that we are going to use in this tutorial.
Link : https://api.zksync.io/api/v0.2/ - mainnet api v0.2
And also we will use python language beacuse most of the Data Scientists and particapents of hackathon use python as the main tool for development.


## Source Code and Implementation: 
We will use api v0.2 of zksync for getting transactions data which is a rest API and you can find docs here : https://docs.zksync.io/apiv02-docs/
There are a lot of endpoints for different purposes but for this tutorial our focus will be on getting transactions data of one specific account in blockchain, which is very important for hackathon participants to use this for sybil detection algorithms etc.

before starting to explain the source code we need to install requests package, that we will be using to working with APIs with this commend : 
```
pip install requests 
```
Now lets dive into the zksync.py code: 

``` 

from requests import get

class ZkTrack:

    def __init__(self, address) -> None:
        self.address = address
        self.BASE_URL = "https://api.zksync.io/api/v0.2/"
    def create_api_url(self,module, address, action, tags):
        
        
        url = self.BASE_URL + f"{module}/{address}/{action}?"
        for key, value in tags.items():
            url += f"&{key}={value}"
        return url

    def get_transfers(self):
        url = self.create_api_url("accounts", self.address, "transactions", {'from':'latest', 'limit':70, 'direction':'older'})
        request = get(url)
        response = request.json()['result']['list']

        transactions = []
        for tx in response:
            
            if tx['op']['type'] == 'Transfer': 
                tx_doc = {}
                tx_doc['from'] = tx['op']['from']
                tx_doc['to'] = tx['op']['to']
                tx_doc['fee'] = int(tx['op']['fee']) / 10**18
                tx_doc['status'] = tx['status']
                tx_doc['createdAt'] = tx['createdAt']
                transactions.append(tx_doc)            

        return transactions
    def get_balance(self):
        url = self.BASE_URL + f"accounts/{self.address}"
        request = get(url)
        response = request.json()
        return response['result']['committed']['balances']['ETH']

 ```
 
 For using this script first clone the repo and import the ZkTrack to your codebase and then you are good to go and use methods: 
 ```
 from zksync import ZkTrack 
 ```
 Then you should create an instace of ZkTrack class
 ```
 account_1 = ZkTrack("#address")
 ```
 For retrieving transactions of a specific account : 
 ```
 transactions = account_1.get_transfers()
 ```
 For getting balance of an account: 
 ```
 balance = account_1.get_balance()
 ```
 summary of code : 
 ```
 from zksync import ZkTrack
 account_1 = ZkTrack("#your_address")
 transactions = account_1.get_transfers()
 balance = account_1.get_balance()
 ```
