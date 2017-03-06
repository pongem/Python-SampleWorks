# credit code adapt from K. Gant
# https://lifeonvm.nkuln.com/?p=29

import csv

from mod_SET_Helper import *



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
            outputFile = open('./data/%s.csv' % stock, 'w')
            outputWriter = csv.writer(outputFile)

            # header
            outputWriter.writerow(["Date","Open","High","Low","Close","Volume","Adj Close"])

            # write data into csv
            for record in records:
                # print( "data %s %s %s %s %s %s %s" % ( record.date.strftime("%Y-%m-%d"), record.open, record.max, record.min, record.close,record.volume, None ) )
                outputWriter.writerow([record.date.strftime("%Y-%m-%d"), record.open, record.max, record.min, record.close,record.volume, None])


