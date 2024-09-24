import sys
from ibapi.client import *
from ibapi.common import TickAttrib, TickerId
from ibapi.ticktype import TickType
from ibapi.wrapper import *
from ibapi.contract import ComboLeg
from ibapi.tag_value import TagValue
import time


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        mycontract = [Contract()]

        mycontract[0].symbol = "GC"
        mycontract[0].secType = "BAG"   # Indicates we wish to use a combo
        mycontract[0].currency = "USD"
        mycontract[0].exchange = "SMART"

        leg1 = ComboLeg()
        leg1.conId = 726219326
        leg1.ratio = 1
        leg1.action = "SELL"
        leg1.exchange = "COMEX"

        leg2 = ComboLeg()
        leg2.conId = 726219106
        leg2.ratio = 1
        leg2.action = "SELL"
        leg2.exchange = "COMEX"

        leg3 = ComboLeg()
        leg3.conId = 726219237
        leg3.ratio = 1
        leg3.action = "BUY"
        leg3.exchange = "COMEX"

        leg4 = ComboLeg()
        leg4.conId = 726219652
        leg4.ratio = 1
        leg4.action = "BUY"
        leg4.exchange = "COMEX"

        mycontract[0].comboLegs = []
        mycontract[0].comboLegs.append(leg1)
        mycontract[0].comboLegs.append(leg2)
        mycontract[0].comboLegs.append(leg3)
        mycontract[0].comboLegs.append(leg4)

        self.reqMarketDataType(3)
        self.reqMktData(orderId, mycontract[0], "", 0, 0, [])


    def  tickPrice(self, reqId, tickType, price, attrib):
        print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}")



app = TestApp()
app.connect("localhost", 7497, 400)
app.run()