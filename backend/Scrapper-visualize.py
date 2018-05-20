
# coding: utf-8

# In[44]:


# In[76]:



import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pymysql
#plt.rcParams['figure.figsize'] = [15, 10]


# In[77]:


db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()


# In[78]:


#cursor.execute("""select * from allergens""")
#print(cursor.fetchall())


# In[79]:


#cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL 1 DAY) AND DATE(NOW())""")
#results5=cursor.fetchall()
#cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL 2 DAY) AND DATE(NOW() - INTERVAL 1 DAY)""")
#results4=cursor.fetchall()
#cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL 3 DAY) AND DATE(NOW() - INTERVAL 2 DAY)""")
#results3=cursor.fetchall()
#cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL 4 DAY) AND DATE(NOW() - INTERVAL 3 DAY)""")
#results2=cursor.fetchall()
#cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL 5 DAY) AND DATE(NOW() - INTERVAL 4 DAY)""")
#results1=cursor.fetchall()


# In[80]:


#allergen_name= 'Ascopores'
allergen_name= 'cladosporium'
cursor.execute("""select * from allergens WHERE allergen_name = '%s' ORDER BY created_date"""%allergen_name)
results=cursor.fetchall()
#results


# In[81]:


day=np.arange(5)
results2=np.zeros(5)
results2
for i in range(len(results)):
   results2[i]=results[i]['count']


# In[82]:


#results2


# In[83]:


#plt.cla()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(day, results2, 1.0, color='deepskyblue')
ax.set_xlabel('day',fontsize = 20)
ax.set_ylabel('Pollen in Cubic Meter Air',fontsize = 20)
ax.set_title(allergen_name,fontsize = 20)
plt.savefig('week'+allergen_name+'.png',bbox_inches='tight',dpi=200)


# In[84]:


db.close()

