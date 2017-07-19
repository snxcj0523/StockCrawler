import scrapy
import csv
StockID='3003'
class StockPrice(scrapy.Spider):
    name = "StockPrice"
    
    def start_requests(self):
        global StockID
        StockID=str(self.ID)
        self.log(self.ID)
        self.log(StockID)
        self.log("-------------------")
        link='http://www.cnyes.com/twstock/ps_historyprice/' + StockID + '.htm'
        yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        my_list=response.xpath('//div[@class="mbx bd3"]//div[@class="tab"]//td/text()').extract()
        idx=0
        a=my_list
        b=[["股票代碼",StockID,"一個月內股價"], ["日期", "開盤", "收盤", "漲跌(%)"]] 
        dx=int(len(my_list)/10)
        for x in range(dx):
            c=[a[0+x*10], a[1+x*10], a[4+x*10], a[6+x*10]]
            b.append(c)
            self.log(x)
        self.log("mylistsize")
        self.log(len(my_list))
        f = open("E "+StockID+".csv","w")
        w = csv.writer(f)
        w.writerows(b)
        f.truncate()
        f.close()
        