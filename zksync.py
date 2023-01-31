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

if __name__ == '__main__':
    account_1 = ZkTrack("0x45b381A5b6eD9312926c1faC846696D33AE1C0dB")
    txns = account_1.get_transfers()
    account_balance = account_1.get_balance()
    