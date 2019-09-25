from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

class Laravelnews:
	def __init__(self):
		self.base = "https://laravel-news.com"
		self.result =pd.DataFrame()

	def scrap_it_packages(self):
		scraping_result = []
		halaman = Request("{}/category/laravel-packages".format(self.base),headers={'User-Agent': 'Mozilla/5.0'})
		buka_halaman = urlopen(halaman).read()
		soup = BeautifulSoup(buka_halaman,'html.parser')
		content = soup.select("div.card.w-full.card--post.mx-0")
		for c in content:
		    scarp = BeautifulSoup(r"{}".format(c),"html.parser")
		    image = scarp.select_one("div.post__image > a > img")
		    title = scarp.select_one("h2.text-2xl > a")
		    url = r"{}{}".format(self.base,title["href"])
		    desc = scarp.select_one("p").text
		    date = scarp.select_one("div.post__content > span > span:nth-child(2)").text
		    body = self.scrap_it_detail(url)
		    scraping_result.append({
		        "images":image["src"],
		        "title":title.text,
		        "desc":desc,
		        "date":date,
		        "url":url,
		        "sources":self.base,
		        "body":body
		    })

		scraping_result = pd.DataFrame(scraping_result)
		self.result = pd.concat([self.result,scraping_result], ignore_index=True, sort=False)

	def scrap_it_article(self):
		scraping_result = []
		halaman = Request("{}/category/laravel-tutorials".format(self.base),headers={'User-Agent': 'Mozilla/5.0'})
		buka_halaman = urlopen(halaman)
		s = BeautifulSoup(buka_halaman,'html.parser')
		content = s.select("div.items-start > a.card")
		for c in content:
			sc = BeautifulSoup(r"{}".format(c),"html.parser")
			image = sc.select_one("div.card__image > img")
			title = sc.select_one("div.card__content > h4").text
			url = r"{}{}".format(self.base,c["href"])
			date = sc.select_one("div.card__content > span.label").text
			body = self.scrap_it_detail(url)
			scraping_result.append({
					"images":image["src"],
					"title":title,
					"desc":title,
					"date":date,
					"url":url,
					"sources":self.base,
					"body":body
				})

		scraping_result = pd.DataFrame(scraping_result)
		self.result = pd.concat([self.result,scraping_result], ignore_index=True, sort=False)

	def scrap_it_blog(self):
		scraping_result = []
		halaman = Request("{}/blog".format(self.base),headers={'User-Agent': 'Mozilla/5.0'})
		buka_halaman = urlopen(halaman).read()
		soup = BeautifulSoup(buka_halaman,'html.parser')
		content = soup.select("div.card.w-full.card--post.mx-0")
		for c in content:
		    scarp = BeautifulSoup(r"{}".format(c),"html.parser")
		    image = scarp.select_one("div.post__image > a > img")
		    title = scarp.select_one("h2.text-2xl > a")
		    url = r"{}{}".format(self.base,title["href"])
		    desc = scarp.select_one("p").text
		    date = scarp.select_one("div.post__content > span > span:nth-child(2)").text
		    body = self.scrap_it_detail(url)
		    scraping_result.append({
		        "images":image["src"],
		        "title":title.text,
		        "desc":desc,
		        "date":date,
		        "url":url,
		        "sources":self.base,
		        "body":body
		    })

		scraping_result = pd.DataFrame(scraping_result)
		self.result = pd.concat([self.result,scraping_result], ignore_index=True, sort=False)

	def scrap_it_detail(self,url):
		halaman = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
		buka_halaman = urlopen(halaman).read()
		soup = BeautifulSoup(buka_halaman,'html.parser')
		body = soup.select_one("div.post__content > div.w-full > p")

		return r"{}".format(body)
		

