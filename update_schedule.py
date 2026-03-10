import requests
from bs4 import BeautifulSoup
import json

buses=[]

# HAVAS
url="https://www.e-yasamrehberi.com/havas/havas_dalaman_havalimani.htm"

soup=BeautifulSoup(requests.get(url).text,"html.parser")

for tr in soup.select("table tr"):

    td=tr.find_all("td")

    if len(td)>1:

        times=td[1].get_text().split(",")

        for t in times:

            t=t.strip()

            if ":" in t:

                buses.append({
                "time":t,
                "company":"Havas"
                })


# MUTTAS
url="https://ulasim.muttas.com.tr/hat/48-25-fethiye-otogar-dalaman-havalimani-439"

soup=BeautifulSoup(requests.get(url).text,"html.parser")

for tr in soup.select("table tr"):

    td=tr.find("td")

    if td:

        t=td.get_text().strip()

        if ":" in t:

            buses.append({
            "time":t,
            "company":"Muttas"
            })


with open("schedule.json","w",encoding="utf8") as f:

    json.dump(buses,f,ensure_ascii=False,indent=2)
