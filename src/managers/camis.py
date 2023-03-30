import time
import requests
from bs4 import BeautifulSoup


USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
headers = {"User-Agent": USER_AGENT}
url = 'http://41.205.64.173/'
response = requests.get(url, headers=headers)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('td')
    print("###################")
    print(title.text)
else:
    print("rien")

