import scrapy

class questao1(scrapy.Spider):

    name = 'questao1'
    start_urls = {
        'https://www.uol.com.br/'
    }

    def parse(self, response):

        dolar = response.xpath('//*[@id="HU_header"]/div[2]/div/div[2]/div[2]/ul/li[1]/a/span[2]/text()').extract_first()
        print("Cotação do dolar: R$ {}".format(len(dolar)))
        
        yield {
            'Cotacao do dolar: R$ ': dolar
        }

