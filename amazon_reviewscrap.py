from bs4 import BeautifulSoup as bs
import requests

link = 'https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJHV6VZ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(link)
page.content
soup = bs(page.content, 'html.parser')
names = soup.find_all('span', class_='a-profile-name')
cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name.pop(0)
cust_name.pop(0)

title = soup.find_all('a',class_='review-title-content')
review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:] = [titles.lstrip('\n') for titles in review_title]
review_title
review_title[:] = [titles.rstrip('\n') for titles in review_title]
review_title
rating = soup.find_all('i',class_='review-rating')
rating
rate = []
for i in range(0, len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.pop(0)
rate.pop(0)
rate
review = soup.find_all("span",{"data-hook":"review-body"})
review
review_content = []
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content
review_content[:] = [reviews.lstrip('\n') for reviews in review_content]
review_content
review_content[:] = [reviews.rstrip('\n') for reviews in review_content]
review_content
len(review_content)
cust_name
review_title
rate
review_content
import pandas as pd
df = pd.DataFrame()
df
df['Customer Name']=cust_name
df
df['Review title']=review_title
df['Ratings']=rate
df['Reviews']=review_content
done
df
df.to_csv(r'E:\reviews.csv', index=True)