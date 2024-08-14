from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId:int):
        mycontract = Contract()
        mycontract.symbol = "YM"
        mycontract.secType = "FUT"
        mycontract.exchange = "CBOT"
        mycontract.currency = "USD"
        mycontract.multiplier = "5"
        mycontract.lastTradeDateOrContractMonth = "202409"

        self.reqContractDetails(orderId, mycontract)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print(contractDetails.contract)

        myorder = Order()
        myorder.orderId = reqId
        myorder.action = "BUY"
        myorder.orderType = "MKT"
        myorder.totalQuantity = 1
        myorder.tif = "GTC" 
        myorder.account = "DU7293956"
       
        self.placeOrder(reqId, contractDetails.contract, myorder)
 

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order,orderState: OrderState):
        print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")
        print("openOrder")

    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print(f"orderStatus. orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}")
        print("orderStatus")


    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"execDetails. reqId: {reqId}, contract: {contract}, execution: {execution}")
        print("ExecDetails")
        self.disconnect()



app = TestApp()
app.connect("127.0.0.1", 7497, 1000)
app.run()