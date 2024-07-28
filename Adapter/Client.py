from Adapter.ICICINetBanking import ICICINetBanking
from Adapter.NetBanking import NetBanking
from Adapter.YESNetBanking import YesNetBanking


class Client:
    if __name__ == '__main__':
        myBank = YesNetBanking()
        myBank.authenticate()
        myBank.checkBalance()
        myBank.transferMoney()
