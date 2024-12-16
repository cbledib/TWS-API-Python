from ibapi.client import *
from ibapi.common import TickAttrib, TickerId
from ibapi.ticktype import TickType
from ibapi.wrapper import *


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        mycontract = Contract()

        mycontract.symbol = "AAPL"
        mycontract.exchange = "SMART"
        mycontract.secType = "STK"
        mycontract.currency = "USD"

        self.reqMarketDataType(3)
        self.reqMktData(orderId, mycontract, "", 0, 0, [])
    
    def tickSize(self, reqId, tickType, size):
        print(f"tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}")

    def  tickPrice(self, reqId, tickType, price, attrib):
        print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}")

app = TestApp()
app.connect("localhost", 7497, 400)
app.run()