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
        mycontract.secType = "OPT"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"
        mycontract.lastTradeDateOrContractMonth = "20240719"
        mycontract.strike = 215
        mycontract.right = "P"  # Put so only OPTION_PUT_OPEN_INTEREST will return a value in this case
        mycontract.multiplier = "100"
        mycontract.tradingClass = "AAPL"
    
        self.reqMarketDataType(3)
        self.reqMktData(orderId, mycontract, "101", 0, 0, []) # Request for Generic Tick 101 to return OPTION_CALL_OPEN_INTEREST & OPTION_PUT_OPEN_INTEREST

    
    def tickSize(self, reqId, tickType, size):
        print(f"tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}")
        

app = TestApp()
app.connect("localhost", 7497, 1000)
app.run()
