import math, requests, json
from scrapy.http import HtmlResponse
import pandas as pd

raw_dataframe = [ ]

res = requests.get('https://www.amazon.com/Moto-Alexa-Hands-Free-camera-included/product-reviews/B07N9255CG?ie=UTF8&reviewerType.all_reviews')

response = HtmlResponse(url=res.url, body=res.content)

product_name = response.xpath('//h1/a/text()').extract_first(default=' ').strip()

total_reviews = response.xpath('//span[contains(text(),"Showing")]/text()').extract_first(default=' ').strip().split()[-2]

total_pages = math.ceil(int(total_reviews)/10)

for i in range(0,total_pages):
    url = f"https//www.amazon.com/hz/reviews-render/ajax/reviews/get/ref=cm_crarp_d_paging_btm_next_{str(i+2)}"
    head = {'accept': 'text/html, */*',
    'accept-encoding': 'gzip,deflate,br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'origin': 'https://www.amazon.com',
    'referer':response.url,
    'user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KWH, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'x- requested-with': 'XMLHttpRequest'
}

payload = {'reviewerType':'all_reviews',

'pageNumber': i+2,

'shouldAppend': 'undefined',

'reftag': 'cm_crarp_d_paging_btm_next_{str(i+2))',

'pageSize': 10,

'asin': '807N9255C',

}

res = requests.post(url,headers=head,data=json.dumps(payload))

response = HtmlResponse(url=res.url, body=res.content)

loop = response.xpath('//div[contains(@class,"a-section review")]')

for part in loop:
    review_title = part.xpath('.//a[contains(@Class,"review-title-content")]/span/text()').extract_first(default=' ').strip()
    rating =part.xpath('.//a[contains(@title,"out of 5 stars")]/@title').extract_first(default=' ').strip().split()[0].strip()
    reviewername = part.xpath('.//span[@class."a-profile-name"]/text()').extract_first(default=' ').strip()
    description =''.join(part. xpath('.//span[contains(@class,"review-text-content")]/span/text()') .extract()).strip()
    helpful_count =part.xpath('.//span[contains(@class,"cr-vote-text")]/ text()').extract_first(default ='').strip().split()[0].strip()
    raw_dataframe.append([product_name,review_title,rating,reviewer_name, description,helpful_count])

df =pd.Dataframe,(raw_dataframe,columns['Product Name','Review Title','Review Rating','Reviewer Name','Description','Helpful Count' ]),

#exporting csv

df.to_csv("amazon reviews.csv",index=None)