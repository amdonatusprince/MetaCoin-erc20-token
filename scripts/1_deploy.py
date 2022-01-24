from brownie import DemoCoin, ConvertLib, accounts, config

account = accounts.add(config["wallets"]["from_key"])
lib = ConvertLib.deploy({"from": account})
transaction = DemoCoin.deploy({"from": account})

def get_balance():
    balance = transaction.getBalance(account)
    print(f'The available balance for {account} is {balance}')
    

def send_coin():
    txt = transaction.sendCoin('0x18207c897212c0F9886b4f27133f54b14cA4db0C', 500)
    print(txt)


def main():
    get_balance()
    send_coin()
    get_balance()
