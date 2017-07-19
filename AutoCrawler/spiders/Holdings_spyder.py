import scrapy
import csv
StockID='3015'
class Holdings(scrapy.Spider):
    name = "Holdings"
    
    def start_requests(self):
        global StockID
        StockID=str(self.ID)
        self.log(self.ID)
        self.log(StockID)
        self.log("-------------------")
        link='http://goodinfo.tw/StockInfo/EquityDistributionClassHis.asp?STOCK_ID=' + StockID
        yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        my_list=response.xpath('//table[@class="solid_1_padding_3_0_tbl"]//nobr//text()').extract()
        self.log(my_list)
        a=my_list[24:240]
        b=[["股票代碼",StockID,"各持股等級股東之持股比例(%)"], ["月份", "400~800", "800~1K", "1K up"]]
        try:
            for x in range(18):
                c=[a[0+x*12], a[9+x*12], a[10+x*12], a[11+x*12]]
                b.append(c)
        except IndexError:
            self.log("IndexError, No Valid Data.")
        self.log(b)
        f = open("A "+StockID+".csv","w")
        w = csv.writer(f)
        w.writerows(b)
        f.truncate()
        f.close()
            

