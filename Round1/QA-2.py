# WAP to get the Social Links, Email & Contacts details of a website on user input.

import re
import requests
import bs4

result = requests.get("https://ful.io")

# print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')

social_links = soup.find_all('a', attrs={'href': re.compile("^https://")})

social_links_linkedIn = social_links[-1].get('href')
social_links_Facebook = social_links[-2].get('href')

print(f'LinkedIn - {social_links_linkedIn}')
print(f'Facebook - {social_links_Facebook}')

Contact = soup.select('p')[-2].getText()
print(f'Contact - {Contact}')

Emails = soup.select('a')[-2].getText()
print(f'Emails - {Emails}')