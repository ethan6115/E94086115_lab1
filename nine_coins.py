class Nine_Coins:
    
    def __init__(self,number):                                
        self.number=number                                       #記住輸入的值
        self.binary='{0:0>9b}'.format(number)                    #用format把輸入值轉為二進位
        listbinary=list(str(self.binary))                        # 將二進位轉成string的list
        coin=str()                                               #創造coin來記住硬幣正反面
        for i in range(0,9):
                if listbinary[i]=='1':                           #當二進位值為1時coin加上T
                    coin+='T'
                else:                                            #當二進位值為0時coin加上H
                    coin+='H'
        self.coin=coin
    def toss(self):
        import random                                            #和上面一樣作法只是將輸入改由random得出
        number=random.randint(0, 512)
        self.number=number
        self.binary='{0:0>9b}'.format(number)  
        listbinary=list(str(self.binary))
        coin=str()
        for i in range(0,9):
                if listbinary[i]=='1':
                    coin+='T'
                else:
                    coin+='H'
        self.coin=coin
    def __repr__(self):
        return(f'Nine_coins: {self.coin}')                       
    def __str__(self):
        return(f'binary: {self.binary} and decimal: {self.number}')   