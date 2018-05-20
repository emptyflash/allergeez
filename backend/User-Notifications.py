
# coding: utf-8

# In[72]:


#get_ipython().system('pip3 install beautifulsoup4')
#get_ipython().system('pip3 install requests')
#get_ipython().system('pip3 install lxml')


# In[153]:


from bs4 import BeautifulSoup
import requests
from datetime import datetime


# In[154]:


import pymysql


# In[155]:


db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()


# In[156]:


cursor.execute("""select * from subscriptions""")
cursor.fetchall()


# In[157]:


for num_days in range(10):
  #print("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
  cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
  results=cursor.fetchall()
  if len(results)>0:
        break;

results


# In[158]:


tree_keys=['maple', 'mulberry', 'alder', 'pine', 'birch', 'sycamore', 'hickory', 'cottonwood', 'hackberry', 'oak', 'hazelnut', 'willow', 'cedar', 'linden', 'ash', 'elm', 'walnut', 'sweetgum', 'other tree']
weed_keys=['ragweed', 'plantain', 'sage', 'sheep', 'aster', 'cattail', 'amaranth', 'nettle', 'sedge', 'other']
mold_keys=['algae', 'erysiphe', 'alternaria', 'aspergillus', 'ascopores', 'periconia', 'basidiospores', 'pithomyces', 'cercospora', 'rusts', 'cladosporium', 'myxomycetes', 'curvularia', 'spegazzinia', 'helminthosporium', 'stemphilium', 'epicoccum', 'tetraploa', 'nigrospora', 'torula']


# In[161]:


res_all=[]


# In[162]:


for key in tree_keys:
  treshold_reached=0
  for i in range(len(results)):
      if results[i]['allergen_name']==key:  
        treshold_num=results[i]['count']
        if results[i]['count']>0:
          treshold_reached=1
        if results[i]['count']>14:
          treshold_reached=2
        if results[i]['count']>89:
          treshold_reached=3
        if results[i]['count']>1499:
          treshold_reached=4
  #print(key, treshold_reached, treshold_num)
  treshold_reached=1
  if treshold_reached==1:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low') AND allergen_name = '%s'""" % key)
  if treshold_reached==2:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium') AND allergen_name = '%s'""" % key)
  if treshold_reached==3:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy') AND allergen_name = '%s'""" % key)
  if treshold_reached==4:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy','extremely heavy') AND allergen_name = '%s'""" % key)
  res=cursor.fetchall()
  if len(res)>0:
    #print("alert for", key, " ", res)
    res_all=res_all+res


# In[163]:


for key in weed_keys:
  treshold_reached=0
  for i in range(len(results)):
      if results[i]['allergen_name']==key:  
        treshold_num=results[i]['count']
        if results[i]['count']>0:
          treshold_reached=1
        if results[i]['count']>4:
          treshold_reached=2
        if results[i]['count']>19:
          treshold_reached=3
        if results[i]['count']>200:
          treshold_reached=4
  #print(key, treshold_reached, treshold_num)
  treshold_reached=1
  if treshold_reached==1:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low') AND allergen_name = '%s'""" % key)
  if treshold_reached==2:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium') AND allergen_name = '%s'""" % key)
  if treshold_reached==3:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy') AND allergen_name = '%s'""" % key)
  if treshold_reached==4:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy','extremely heavy') AND allergen_name = '%s'""" % key)
  res=cursor.fetchall()
  if len(res)>0:
    print("alert for", key, " ", res)
    res_all=res_all+res


# In[164]:


for key in mold_keys:
  treshold_reached=0
  for i in range(len(results)):
      if results[i]['allergen_name']==key:  
        treshold_num=results[i]['count']
        if results[i]['count']>0:
          treshold_reached=1
        if results[i]['count']>6499:
          treshold_reached=2
        if results[i]['count']>12999:
          treshold_reached=3
        if results[i]['count']>49999:
          treshold_reached=4
  #print(key, treshold_reached, treshold_num)
  treshold_reached=1
  if treshold_reached==1:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low') AND allergen_name = '%s'""" % key)
  if treshold_reached==2:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium') AND allergen_name = '%s'""" % key)
  if treshold_reached==3:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy') AND allergen_name = '%s'""" % key)
  if treshold_reached==4:
    cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy','extreme') AND allergen_name = '%s'""" % key)
  res=cursor.fetchall()
  if len(res)>0:
    print("alert for", key, " ", res)
    res_all=res_all+res


# In[165]:


#res_all


# In[166]:


unique_user=set()
for res in res_all:
    #print(res['user_id'])
    if res['user_id'] not in unique_user:
        unique_user.add(res['user_id'])


# In[167]:


for user in unique_user:
    alerts_user=[]
    for res in res_all:
       #print(res['user_id'])
       if res['user_id']==user:
            alerts_user.append(res['allergen_name'])
    print("alert user ",user," for ", alerts_user)
            


# In[168]:


db.close()

