# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from bs4 import BeautifulSoup


# %%
# r=requests.get("https://www.century21.com/real-estate/san-francisco-ca/LCCASANFRANCISCO/")

r=requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content


# %%
soup=BeautifulSoup(c,"html.parser")
# print(soup.prettify())


# %%
all=soup.find_all("div", {"class":"logo"})  


# %%
all


# %%
all=soup.find_all("div", {"class":"filters-container"})


# %%
all


# %%
all=soup.find_all("div", {"class":"full-width-container"})  


# %%
all


# %%
all=soup.find_all("div", {"class":"property-actions"}) 


# %%
all


# %%
type(all)


# %%
len(all)


# %%
all[0]


# %%
all1=soup.find_all("div", {"class":"infinite-container"})


# %%
# all1
all1=soup.find("div", {"class":"infinite-container"})
print(all1.text)


# %%
# all1[0].find_all("a", {"class":"listing-price"})
# for item in range(0,10):
all1[0].find_all("a", {"class":"listing-prices"})


# %%
all1[0].find("a", {"class":"listing-price"}).text


# %%
type(all1[0].find("a", {"class":"listing-price"}).text)


# %%
all1[0].find("a", {"class":"listing-price"}).text.replace("\n", "")


# %%
# all1[0].find("a", {"class":"listing-price"}).text.replace("\n", "").replace(" ", "")

all1[0].find("a", {"class":"listing-price"}).text.replace("\n", "").replace(" ", "")


# %%
all1


# %%
all1


# %%
for item in all1:
    print(item.find("a", {"class":"infinite-containers"}).text.replace("\n", "").replace(" ", ""))


# %%
all1.find_all("a", {"class":"listing-price"})
all1.text.replace("\n", "").replace(" ", "")


# %%
import requests
from bs4 import BeautifulSoup

r= requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c=r.content

soup=BeautifulSoup(c,"html.parser")

all4=soup.find("div", {"class":"infinite-container"})
len(all4)
# all4.find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ","")


# %%
# type(all4)
all4


# %%
# len(all4.find_all("a"))
# all4.find("a")


# %%
len(all4)


# %%
# all4.find_all("a")[0].text.replace("\n","").replace(" ","")
# all4.find("a").text

all4.find_all("a")[0]

for item in range(0,9):
    print(all4.find_all("a")[item].text.replace("\n","").replace(" ",""))


# %%
# for item in all4:
#     print(item.find("a").text.replace("\n","").replace(" ",""))
# all4.find_all("a")
# all4=all4.find_all("a")


# %%
# for item in range(len(all4.find_all("a"))):
# for item in range(0,9):
    # print(all4.find("a"))
    # print(all4.find_all("a"))
print(all4.find_all("a"))
len(all4)


# %%
for item in range(0,20):
    all4.find("a").text.replace("\n", "").replace(" ", "")


# %%
import requests
from bs4 import BeautifulSoup
    # print(all4.find_all("a")[item].text.replace("\n","").replace(" ",""))


r= requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all5=soup.find_all("div", {"class":"property-address"})
# all5.find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ","")


# %%
print(all5[0].text.replace("\n","").replace(" ",""))
len(all5)
print(all5)


# %%
# for value in range(0,9):
for value in range(len(all5)):
    print(all5[value].text.replace("\n","").replace(" ",""))
    # print(all5)


# %%
#import requests
from bs4 import BeautifulSoup

r= requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all6=soup.find_all("div", {"class":"property-beds"})
all7=soup.find_all("div", {"class":"property-baths"})


# %%
print(all6)
len(all6)

print(all7)
len(all7)


# %%
l=[]

for value in range(len(all6)):
    d={}
    # d["Address"]=all5[value].text.replace("\n","").replace(" ","")
    d["Address"]=all5[value].text.replace("\n","")
        # d["Beds"]=all6[value].text
    d["Beds"]=all6[value].text.replace("\n","").replace(" ", "")
    d["Baths"]=all7[value].text.replace("\n","").replace(" ", "")
    # print(all4.find_all("a")[item].text.replace("\n","").replace(" ",""))
    # d["Price"]=all4.find_all("a")[item].text.replace("\n","").replace(" ","")
    d['Price']=all4.find_all("a")[value].text.replace("\n","").replace(" ","")
    # d["Baths"]=all7[value].text
    # d[]=(" ")
    l.append(d)


# %%
l


# %%
import pandas
# df = data frame
df=pandas.DataFrame(l)


# %%
df


# %%
df.to_csv("Output2.csv")


# %%



