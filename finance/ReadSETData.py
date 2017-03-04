# credit code adapt from K. Gant
# https://lifeonvm.nkuln.com/?p=29

from urllib.request import urlopen
from decimal import Decimal
from bs4 import BeautifulSoup

import csv
from datetime import datetime

class DayData:
    date = None
    open = None
    close = None
    max = None
    min = None
    volume = None
    value = None
    set_index = None

    def __init__(self):
        pass

    @staticmethod
    def to_datetime(str):
        from datetime import datetime
        ds = [int(x) for x in str.split('/')]
        ds[2] = ds[2] + 2000
        return datetime(ds[2], ds[1], ds[0])
                
    @staticmethod
    def to_decimal(str):
        from decimal import Decimal
        return Decimal(str.replace(',',''))

class SETFetch:

    def __init__(self):
        self.set_stockdata_url = "http://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=%s&selectPage=null&max=15&offset=%d";
        self.set100_url = "http://www.settrade.com/C13_MarketSummary.jsp?detail=SET100"

    def fetchSet100(self):
        page = urlopen(self.set100_url)
        soup = BeautifulSoup(page, "html.parser")

        stocks = soup.findAll("a", {"class": "link-stt"})

        arrSTocks = []
        for stock in stocks :
            if (stock.text.find("SET") < 0):
                #print( stock.text )
                arrSTocks.append( stock.text )
        return arrSTocks

    def fetchDataStock(self,symbol):
        
        cur_pos = 1
        all_data = []

        while True:
            #print ( self.set_stockdata_url % (symbol, cur_pos * 15) )
            page = urlopen( self.set_stockdata_url % (symbol, cur_pos * 15))
            soup = BeautifulSoup(page, "html.parser")

            # need code this change if settrade change to display data more than 15
            # get content body
            read_data = None
            contents = soup.findAll( 'tbody' )
            for content in contents :
                body = content.findAll('tr')
                if ( len (body) == 15 ) :
                    read_data = body
                    #print("Grab it!")

            if read_data == None:
                # no more data to read
                break
            cur_pos = cur_pos + 1
            all_data = all_data + read_data

        daily = []
        for day in all_data:
            flds = day.findAll('td')
            current = DayData()
            try:
                current.date =  DayData.to_datetime(flds[0].text)
                current.open = DayData.to_decimal(flds[1].text)
                current.max = DayData.to_decimal(flds[2].text)
                current.min = DayData.to_decimal(flds[3].text)
                current.close = DayData.to_decimal(flds[5].text)
                current.volume = DayData.to_decimal(flds[8].text) * 1000
                current.value = DayData.to_decimal(flds[9].text)
                current.set_index = DayData.to_decimal(flds[10].text)
                daily.append(current) 
            except Exception as e:
                print ("error formatting data")
                pass
            finally:
                pass
        daily.sort(key=lambda x: x.date, reverse=True)
        return daily



if __name__ == '__main__':
    

    print ("starting program")

    # get set100
    SETFetchObj = SETFetch()
    arrStocks = SETFetchObj.fetchSet100()

    print ("got total %d stocks" % (len(arrStocks)))

    if ( len ( arrStocks ) > 0) :
        for stock in arrStocks :

            print ( "fechting stock: %s" % ( stock ))
            records = SETFetchObj.fetchDataStock(stock)

            # open csv for write
            outputFile = open('./data/%s.csv' % stock, 'w', newline='')
            outputWriter = csv.writer(outputFile)

            # header
            outputWriter.writerow(["Date","Open","High","Low","Close","Volume","Adj Close"])

            # write data into csv
            for record in records:
                # print( "data %s %s %s %s %s %s %s" % ( record.date.strftime("%Y-%m-%d"), record.open, record.max, record.min, record.close,record.volume, None ) )
                outputWriter.writerow([record.date.strftime("%Y-%m-%d"), record.open, record.max, record.min, record.close,record.volume, None])


