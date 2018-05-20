
# coding: utf-8

# In[8]:




# In[61]:


from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pymysql


# In[62]:


req  = requests.get("http://www.houstontx.gov/health/Pollen-Mold/index.html")
soup = BeautifulSoup(req.text, "lxml")


# In[ ]:



        


# In[63]:


#tree_pollen


# In[64]:


db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()


# In[71]:


for num_days in range(10):
  #print("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
  cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
  results=cursor.fetchall()
  if len(results)>0:
        break;

#print(num_days)


# In[72]:


if len(results)==0:
    print("ERROR no data found")


# In[74]:


identical=True


# In[43]:



tree_pollen={}
table2=soup.find_all('table')[2]
for i in range(20):
    a=table2.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
    a_name=a.split('(')[-1].replace(')','').split(' ')[0].lower()
    if a_name=='other':
        a_name=a_name+' tree'
    if len(a)>0:
        b=table2.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
        #print(a_name,int(b[0]))
        tree_pollen[a_name]=int(b[0])
for key in list(tree_pollen.keys()):
    #print(key)
    for i in range(len(results)):
      if results[i]['allergen_name']==key:  
        if not results[i]['count'] == tree_pollen[key]:
          print(key, results[i]['count'], tree_pollen[key])
          identical=False
          break;
       


# In[44]:


weed_pollen={}
table3=soup.find_all('table')[3]
#table3
for i in range(10):
    a=table3.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
    a_name=a.split('(')[-1].replace(')','').split(' ')[0]
    if len(a)>0:
        b=table3.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
        #print(a,int(b[0]))
        weed_pollen[a_name]=int(b[0])
for key in list(weed_pollen.keys()):
    #print(key)
    for i in range(len(results)):
      if results[i]['allergen_name']==key:  
        if not results[i]['count'] == weed_pollen[key]:
          print(key, results[i]['count'], weed_pollen[key])
          identical=Flase
          break;


# In[46]:


mold_pollen={}
table4=soup.find_all('table')[4]
for i in range(20):
    a=table4.findAll("td", {'width':'35%'})[i].findAll("strong")[0].contents[0].strip()
    if len(a)>0:
        a_name=a.split('/')[-1]
        try:
          b=table4.findAll("td", {'align':'left'})[i].findAll("strong")[0].findAll(text=True)
        except:
          b=table4.findAll("td", {'align':'left'})[i].findAll(text=True)
        b2=[x for x in b if getattr(x, 'name', None) != 'br'][-1]
        mold_pollen[a_name]=int(b2.replace(',' , ''))
        #print(i, a_name,int(b2.replace(',' , '')))
        
for key in list(mold_pollen.keys()):
    #print(key)
    for i in range(len(results)):
      if results[i]['allergen_name']==key:  
        if not results[i]['count'] == mold_pollen[key]:
          print(key, results[i]['count'], mold_pollen[key])
          identical=Flase
          break;


# In[47]:


#identical


# In[49]:


if identical:
    print("DO NOT update, identical")


# In[52]:


if not identical:
    print("DO update")
    time=datetime.now()
    str(time)
    


# In[53]:


if not identical:
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


# In[54]:


if not identical:
    cursor.execute(str_db)
    db.commit()


# In[55]:


#cursor.execute("""select * from allergens""")
#print(cursor.fetchall())


# In[56]:


db.close()

