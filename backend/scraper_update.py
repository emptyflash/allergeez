from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pymysql
import user_notifications
from db import connect_db

req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/index.html")
soup = BeautifulSoup(req.text, "lxml")
db = connect_db()

try:
    with db.cursor() as cursor:
        # Find most recently inserted allergens
        for num_days in range(10):
          cursor.execute("""select * from allergens WHERE DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
          results=cursor.fetchall()
          if len(results)>0:
                break;

        if len(results)==0:
            print("ERROR no data found")

        identical=True

        tree_pollen={}
        table2=soup.find_all('table')[2]
        for i in range(20):
            a=table2.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
            a_name=a.split('(')[-1].replace(')','').split(' ')[0].lower()
            if a_name=='other':
                a_name=a_name+' tree'
            if len(a)>0:
                b=table2.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
                tree_pollen[a_name]=int(b[0])
        for key in list(tree_pollen.keys()):
            for i in range(len(results)):
              if results[i]['allergen_name']==key:
                if not results[i]['count'] == tree_pollen[key]:
                  print(key, results[i]['count'], tree_pollen[key])
                  identical=False
                  break;
               

        weed_pollen={}
        table3=soup.find_all('table')[3]
        for i in range(10):
            a=table3.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
            a_name=a.split('(')[-1].replace(')','').split(' ')[0].lower()
            if len(a)>0:
                b=table3.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
                weed_pollen[a_name]=int(b[0])
        for key in list(weed_pollen.keys()):
            for i in range(len(results)):
              if results[i]['allergen_name']==key:  
                if not results[i]['count'] == weed_pollen[key]:
                  print(key, results[i]['count'], weed_pollen[key])
                  identical=False
                  break;


        mold_pollen={}
        table4=soup.find_all('table')[4]
        for i in range(20):
            a=table4.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
            if len(a)>0:
                a_name=a.split('/')[-1].lower()
                try:
                  b=table4.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
                except:
                  b=table4.findAll("td", {'align':'left'})[i].findAll(text=True)
                b2=[x for x in b if getattr(x, 'name', None) != 'br'][-1]
                mold_pollen[a_name]=int(b2.replace(',' , ''))
                
        for key in list(mold_pollen.keys()):
            for i in range(len(results)):
              if results[i]['allergen_name']==key:  
                if not results[i]['count'] == mold_pollen[key]:
                  print(key, results[i]['count'], mold_pollen[key])
                  identical=False
                  break;

        if identical:
            print("DO NOT update, identical")

        if not identical:
            print("DO update")
            time=datetime.now()
            str(time)
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
            str_db


        if not identical:
            cursor.execute(str_db)
            db.commit()
            user_notifications.retrieve_subs_and_notify(db)

finally:
    db.close()

