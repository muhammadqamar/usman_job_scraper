import pymongo
myclient = pymongo.MongoClient("mongodb+srv://usman:usman@cluster0-h1prq.mongodb.net/test?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE")
mydb = myclient["jobsdata"]
mycol = mydb['jobs']
from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(requests.get('https://news.ycombinator.com/jobs',verify=False).content, "html.parser")
all_job =[]
alltr = soup.find_all("tr",{"class":"athing"})
for x in alltr:
    full_des = x.find('a').text
    try:
      location = full_des.lower().split("in ")[1]
      print (location)
    except:
      location = "NA"
      print (location)
    try:
      company = full_des.lower().split("is hiring")[0]
      print (company)
    except:
      company = "NA"
      print (company)
    try:
      job = full_des.lower().split("is hiring")[1].split("in ")[0]
      print (job)
    except:
      job = "NA"
      print (job)
    dummy = {'company':company,'job':job,'location':location}
    #all_job.append(dummy)

    main_insert = mycol.insert(dummy)
