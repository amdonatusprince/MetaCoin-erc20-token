from scripts.helpful_scripts import get_account
from brownie import MetaCoin
from web3 import Web3

INITIAL_SUPPLY_IN_WEI = Web3.toWei(1000000, "ether")
INITIAL_ETH_SUPPLY = 10**6
RECEIVER_ADDRESS = "0x18207c897212c0F9886b4f27133f54b14cA4db0C"

def deploy_coin():
    account = get_account()
    metacoin = MetaCoin.deploy(INITIAL_ETH_SUPPLY, {"from": account})
    print(f"Token Name: {metacoin.name()}\nToken Symbol: {metacoin.symbol()}\nToken Decomals: {metacoin.decimals()}")
    print(f"Coinbase Balance: {metacoin.balanceOf(account)}")
    print(f"Receiver's Balance: {metacoin.balanceOf(RECEIVER_ADDRESS)}")

    # Transfering 10,000 ETH to an address and then checking the new balance
    metacoin.transfer(RECEIVER_ADDRESS, 10000)
    print(f"Coinbase Balance: {metacoin.balanceOf(account)}")
    print(f"Receiver's Balance: {metacoin.balanceOf(RECEIVER_ADDRESS)} ")

def main():
    deploy_coin()