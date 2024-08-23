# This version is using the Reqmktdata to pull the close price and data

from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import *
import time
import threading
import csv
import re

port = 4001
data = []

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):   
        self.reqPositions() # Request portfolio positions


    def position(self, account: str, contract: Contract, position: Decimal, avgCost: float):
        position = account + "," + str(contract) + "," + str(position) + "," + str(avgCost)
        data.append([position])
        self.defineContracts(data)


    def positionEnd(self):
        self.cancelPositions()
        print("End of positions")


    def defineContracts(self, data):
        x = re.split(r",", str(data[len(data)-1]))  # Split position data for each comma (,)
        # print(f"This is before group: {x}")
    
        # Define contract based off positions pulled
        contract = Contract()
        contract.symbol = x[2]
        contract.secType = x[3]
        contract.exchange = x[8]
        contract.currency = x[10]

        # Request postions market data
        self.reqMarketDataType(3)   # Market data type delayed
        self.reqMktData(len(data)-1, contract, "", 0, 0, [])


    def tickPrice(self, reqId, tickType, price, attrib):
        incomingPrice = TickTypeEnum.to_str(tickType)   # Incoming price type
        if incomingPrice == "CLOSE" or incomingPrice == "DELAYED_CLOSE":    # Only print the close price or delayed_close (if live is not available)
            # Now we want to add the close price to the csv
            data[reqId][0] = data[reqId][0] + "," + str(price)  # Add close to end of each position line
            self.writeToCsv(data)   # Write close to csv


    def writeToCsv(self, data):
        # Write obtained position data to csv file
        with open('test.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
    

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print("Error.", errorCode, errorString, advancedOrderRejectJson)

    
app = TestApp()
app.connect('127.0.0.1', port, 0)
app.run()
