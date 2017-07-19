import scrapy
import csv
StockID='3003'
class Lendings(scrapy.Spider):
    name = "Lendings"
    
    def start_requests(self):
        global StockID
        StockID=str(self.ID)
        self.log(self.ID)
        self.log(StockID)
        self.log("-------------------")
        link='http://www.wantgoo.com/stock/astock/margin?StockNo=' + StockID
        yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        my_list=response.xpath('//div[@id="tab3_list"]//td/text()').extract()
        idx=0
        a=my_list
        b=[["股票代碼",StockID,"30天外資借券賣出餘額變化(張)"], ["日期", "餘額變化(張)"]] 
        for x in range(30):
            c=[a[0+x*6], a[2+x*6]]
            b.append(c)
            self.log(x)
        self.log("mylistsize")
        self.log(len(my_list))
        f = open("B "+StockID+".csv","w")
        w = csv.writer(f)
        w.writerows(b)
        f.truncate()
        f.close()
        my_list2=response.xpath('//div[@id="tab2_list"]//td/text()').extract()
        idx=0
        self.log("mylistsize")
        self.log(len(my_list2))
        a=my_list2
        b=[["股票代碼",StockID,"30天融資券使用率及餘額"], ["日期", "融資餘額(張)", "融資使用率(%)", "融券餘額(張)", "融券使用率(%)"]] 
        for x in range(30):
            c=[a[0+x*10], a[1+x*10], a[3+x*10], a[4+x*10], a[6+x*10]]
            b.append(c)
            self.log(x)
        
        f = open("D "+StockID+".csv","w")
        w = csv.writer(f)
        w.writerows(b)
        f.truncate()
        f.close()
            

