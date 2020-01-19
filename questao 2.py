
import scrapy

class questao2(scrapy.Spider):

    name = 'questao2'

    start_urls = ['https://lista.mercadolivre.com.br/']

    def start_requests(self):
        for url in self.start_urls:
            print(url+self.pesquisa)
            yield scrapy.Request(url+self.pesquisa, dont_filter=True)        

    def parse(self, response):
        produtos = response.xpath('.//ol[contains(@class,"section") and contains(@class,"search-results")]/li')

        for produto in produtos:

            link_detail = produto.xpath('.//a[contains(@class,"item__js-link")]/@href').extract_first()
            #print(link_detail)
            yield scrapy.Request(
                url=link_detail,
                callback=self.parse_detail
            )

        next_page = response.xpath('.//a[contains(@class,"prefetch")]/@href')

        if next_page:
            yield scrapy.Request(
                url=next_page.extract_first(),
                callback=self.parse
            )

    def parse_detail(self, response):

        descricao = (response.xpath('.//h1[contains(@class,"item-title__primary")]/text()').extract_first()).strip()
        preco_inteiro = response.xpath('.//span[@class="price-tag-fraction"]/text()').extract_first()
        preco_decimal = response.xpath('.//span[@class="price-tag-cents"]/text()').extract_first()
        preco = float(preco_inteiro + '.' + ('00' if preco_decimal == none else preco_decimal))

        yield {
            'Produto': descricao,
            'Preco  ': preco
        }