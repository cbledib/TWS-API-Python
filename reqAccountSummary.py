from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, nextId: int):
        self.reqAccountSummary(nextId, "All", 'NetLiquidation,TotalCashValue,MaintMarginReq')

    def accountSummary(self, reqId: TickerId, account: str, tag: str, value: str, currency: str):
        if tag == 'NetLiquidation':
            print('Net Liquidation Value: ', value)
        elif tag == 'TotalCashValue':
            print('Total Cash Value: ', value)
        elif tag == 'MaintMarginReq':
            print('Maintenance Margin Requirement: ', value)

app = TestApp()
app.connect("localhost", 7497, 1000)
app.run()