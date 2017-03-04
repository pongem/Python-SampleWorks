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
    @staticmethod
    def fetch(symbol):
        from urllib.request import urlopen
        from decimal import Decimal
        from bs4 import BeautifulSoup
        
        set_url_format = "http://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol=%s&from=%d";
        cur_pos = 1
        all_data = []

        while True:
            page = urlopen(set_url_format % (symbol, cur_pos))
            print(page.http.client.HPPTResponse)
            soup = BeautifulSoup(page, "html.parser")
            read_data = soup.findAll('tr','tdbg_gray20') + soup.findAll('tr','tdbg_white20')
            if len(read_data) == 0:
                # no more data to read
                break
            cur_pos = cur_pos + len(read_data)
            all_data = all_data + read_data

        daily = []
        for day in all_data:
            flds = day.findAll('td')
            current = DayData()
            current.date =  DayData.to_datetime(flds[0].text)
            current.open = DayData.to_decimal(flds[1].text)
            current.max = DayData.to_decimal(flds[2].text)
            current.min = DayData.to_decimal(flds[3].text)
            current.close = DayData.to_decimal(flds[5].text)
            current.volume = DayData.to_decimal(flds[8].text) * 1000
            current.value = DayData.to_decimal(flds[9].text)
            current.set_index = DayData.to_decimal(flds[10].text)
            daily.append(current)    
        daily.sort(key=lambda x: x.date, reverse=True)
        return daily

if __name__ == '__main__':
    daily = SETFetch.fetch('PTT')
    for day in daily:
        print (day.date)
    #pdb.set_trace()



SETFetchObj = SETFetch()
data = SETFetchObj.fetch('CPF')

print ( data )