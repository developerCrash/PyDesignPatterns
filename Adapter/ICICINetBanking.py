from Adapter.ICICIBankAPI import ICICIBankAPI
from Adapter.NetBanking import NetBanking


class ICICINetBanking(NetBanking):
    def __init__(self):
        self.iciciApi =  ICICIBankAPI()

    def authenticate(self):
        self.iciciApi.whoamI()

    def checkBalance(self):
        self.iciciApi.whatsmybalance()

    def transferMoney(self):
        self.iciciApi.sendmymoney()