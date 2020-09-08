import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

headers_std = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

for x in range(1, 11):
  print(x)
  i=x
  url = 'https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJHV6VZ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i)
  print (url)
  html = requests.get(url, headers=headers_std).text
  soup = BeautifulSoup(html, 'lxml')

  review_title_class = "review-title-content"
  review_date_class = "review-date"
  review_title = soup.findAll("a", {'class': review_title_class})
  review_date = soup.findAll("span", {'class': review_date_class})
  print(review_title[0].text.strip())
  print(review_date[0].text.strip())
  print(len(review_title))
  print(len(review_date))
  review_title_df = []
  review_date_df = []
  for i in range(len(review_title)):
      review_title_df.append(review_title[i].text.strip())
      review_date_df.append(review_date[i].text.strip())
      df = pd.DataFrame({'review_title': review_title_df, 'review_date': review_date_df})
      print(df.head())
      df2 = pd.DataFrame(columns=['title'])
      df2 = df2.append(df)
      with open('output.txt', 'w') as file:

        file.write(str(df2))
  df2.to_csv('amazon_review_page_scraping.csv', index=True, mode='a', header=True)



