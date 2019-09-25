from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

class Kodepolitan:
	def __init__(self):
		self.base = "https://www.codepolitan.com"
		self.result =pd.DataFrame()

	def scrap_it_articles(self):
		scraping_result = []
		halaman = Request("{}/articles".format(self.base),headers={'User-Agent': 'Mozilla/5.0'})
		buka_halaman = urlopen(halaman).read()
		soup = BeautifulSoup(buka_halaman,'html.parser')
		content = soup.select("div.container > div:nth-child(3) > div.col-md-3")
		for c in content:
		    s = BeautifulSoup(r"{}".format(c),"html.parser")
		    image = s.select_one("article.feature > a > img.post-thumb")
		    title = s.select_one("div.feature__body > h4.post-title > a")
		    date = s.select_one("span.post-date")
		    body = self.scrap_it_detail(r"{}".format(title["href"]))
		    scraping_result.append({
		        "images":image["src"],
		        "title":title.text,
		        "desc":title.text,
		        "date":date.text,
		        "url":title["href"],
		        "sources":self.base,
		        "body":body
		    })

		scraping_result = pd.DataFrame(scraping_result)
		self.result = pd.concat([self.result,scraping_result], ignore_index=True, sort=False)

	def scrap_it_detail(self,url):
		halaman = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
		buka_halaman = urlopen(halaman).read()
		soup = BeautifulSoup(buka_halaman,'html.parser')
		body = soup.select_one("div.article__body")

		return r"{}".format(body)