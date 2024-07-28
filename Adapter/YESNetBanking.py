
from Adapter.NetBanking import NetBanking
from Adapter.YesBankAPI import YesBankAPI


class YesNetBanking(NetBanking):
    def __init__(self):
        self.yesApi = YesBankAPI()

    def authenticate(self):
        self.yesApi.authenticate_me()

    def checkBalance(self):
        self.yesApi.checkBalance_me()

    def transferMoney(self):
        self.yesApi.transferMoney_me()