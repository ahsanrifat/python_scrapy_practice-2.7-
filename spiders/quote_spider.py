import scrapy
import pandas as pd

class ToScrapeCSSSpider(scrapy.Spider):
    name = "quote"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    list_of_dict=[]

    def parse(self, response):
        for quote in response.css("div.quote"):
            d={
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }
            print(d)
            self.list_of_dict.append(d)
            yield d
        pd.DataFrame(self.list_of_dict).to_csv("Report.csv",index=False)
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))