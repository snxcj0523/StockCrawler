import scrapy
import csv
StockID='1477'
class netsell(scrapy.Spider):
    name = "netsell"
        
    def start_requests(self):
        global StockID
        StockID=str(self.ID)
        self.log(self.ID)
        self.log(StockID)
        self.log("-------------------")
        link='http://goodinfo.tw/StockInfo/ShowBuySaleChart.asp?STOCK_ID=' + StockID
       
        yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        my_list=response.xpath('//table[@class="solid_1_padding_3_0_tbl"]//td//text()').extract()
        a=my_list[51:409]
        idx=0
        b=[["股票代碼",StockID,"自營商買賣超(張)"], ["期別", "買賣超(張)"]] 
        try:
            for x in range(18):
                c=[a[0+x*19], a[15+x*19]]
                b.append(c)
                self.log(x)
            self.log("mylistsize")
            self.log(len(my_list))
        except IndexError:
            idx=-1
        try:
            idx = my_list.index('比率',idx)+1
        except ValueError:
            idx=-1
        while idx > 0 :
            try:
                idx = my_list.index('比率',idx)+1
                a2=my_list[my_list.index('比率',idx)+13 : my_list.index('比率',idx)+371]
            except ValueError:
                idx=-1
                break
            self.log(idx)
            
            try:
                for x in range(18):
                    c=[a2[0+x*19], a2[15+x*19]]
                    self.log(x)
                    self.log(a2[0+x*19])
                    b.append(c)
            except IndexError:
                self.log("Earliest Date: ")
                self.log(b[-2])
            
                
        self.log(b)
        f = open("C "+StockID+".csv","w")
        w = csv.writer(f)
        w.writerows(b)
        f.truncate()
        f.close()
            

