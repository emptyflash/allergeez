from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pymysql


for day_num in range(14, 19):
    if day_num==14:
        req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/Mondays.html")
    if day_num==15:
        req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/Tuesdays.html")
    if day_num==16:
        req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/Wednesdays.html")
    if day_num==17:
        req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/Thursdays.html")
    if day_num==18:
        req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/Fridays.html")
    soup = BeautifulSoup(req.text, "lxml")

    table1=soup.find_all('table')[1]

    labels=['tree', 'weed','grass','mold']
    for i in range(4):
        table1sel=table1.findAll("td")[i].findAll("strong")[0]
        a=[x.strip() for x in table1sel.contents if getattr(x, 'name', None) != 'br'][-1]
        #print(i, labels[i], int(a.replace(',' , '')))

    table2=soup.find_all('table')[2]

    for i in range(20):
        a=table2.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
        if len(a)>0:
            b=table2.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
            #print(a,int(b[0]))

    tree_pollen={}
    for i in range(20):
        a=table2.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
        a_name=a.split('(')[-1].replace(')','').split(' ')[0].lower()
        if a_name=='other':
            a_name=a_name+' tree'
        if len(a)>0:
            b=table2.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
            #print(a_name,int(b[0]))
            tree_pollen[a_name]=int(b[0])
            
    weed_pollen={}
    table3=soup.find_all('table')[3]
    #table3
    for i in range(10):
        a=table3.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
        a_name=a.split('(')[-1].replace(')','').split(' ')[0].lower()
        if a_name=='other':
            a_name=a_name+' weed'
        if len(a)>0:
            b=table3.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
            #print(a,int(b[0]))
            weed_pollen[a_name]=int(b[0])

    mold_pollen={}
    table4=soup.find_all('table')[4]
    for i in range(20):
        a=table4.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
        if len(a)>0:
            a_name=a.split('/')[-1].lower()
            if a_name=='other':
              a_name=a_name+' mold'
            try:
              b=table4.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
            except:
              b=table4.findAll("td", {'align':'left'})[i].findAll(text=True)
            b2=[x for x in b if getattr(x, 'name', None) != 'br'][-1]
            mold_pollen[a_name]=int(b2.replace(',' , ''))
            #print(i, a_name,int(b2.replace(',' , '')))

    time2=datetime.now()
    time = datetime(time2.year, time2.month, day_num, time2.hour,time2.minute, time2.second ) ;

    str_db="""INSERT INTO `allergens` 
    (`allergen_type`, `allergen_name`, `count`, `created_date`) VALUES """
    for i,(k,v) in enumerate(tree_pollen.items()):
        str_2="""('%s', '%s', %s, '%s'),""" % ('TREE', k,v, time)
        str_db=str_db+str_2

    for i,(k,v) in enumerate(weed_pollen.items()):
        str_2="""('%s', '%s', %s, '%s'),""" % ('WEED', k,v, time)
        str_db=str_db+str_2                                         

    for i,(k,v) in enumerate(mold_pollen.items()):
        str_2="""('%s', '%s', %s, '%s')""" % ('MOLD', k,v, time)
        str_db=str_db+str_2
        if i == (len(mold_pollen)-1):
            str_db=str_db+';'
        else:
            str_db =str_db+','

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         db='db',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    try:
        with db.cursor() as cursor:
            cursor.execute(str_db)
            db.commit()
            print('ok')
    finally:
        db.close()

