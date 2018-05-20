import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     db='db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
try:
    with db.cursor() as cursor:
        for num_days in range(10):
          #print("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
          cursor.execute("""select * from allergens WHERE DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
          results = cursor.fetchall()
          if len(results) > 0:
                break;

        tree_keys = ['maple', 'mulberry', 'alder', 'pine', 'birch', 'sycamore', 'hickory', 'cottonwood', 'hackberry', 'oak', 'hazelnut', 'willow', 'cedar', 'linden', 'ash', 'elm', 'walnut', 'sweetgum', 'other tree']
        weed_keys = ['ragweed', 'plantain', 'sage', 'sheep', 'aster', 'cattail', 'amaranth', 'nettle', 'sedge', 'other']
        mold_keys = ['algae', 'erysiphe', 'alternaria', 'aspergillus', 'ascopores', 'periconia', 'basidiospores', 'pithomyces', 'cercospora', 'rusts', 'cladosporium', 'myxomycetes', 'curvularia', 'spegazzinia', 'helminthosporium', 'stemphilium', 'epicoccum', 'tetraploa', 'nigrospora', 'torula']

        res_all = []

        for key in tree_keys:
          threshold_reached = 0
          reached = "None"
          for i in range(len(results)):
              if results[i]['allergen_name'] == key:  
                threshold_num = results[i]['count']
                if threshold_num > 0:
                  threshold_reached = 1
                  reached = "low"
                if results[i]['count'] > 14:
                  threshold_reached = 2
                  reached = "medium"
                if results[i]['count'] > 89:
                  threshold_reached = 3
                  reached = "heavy"
                if results[i]['count'] > 1499:
                  threshold_reached = 4
                  reached = "extremely heavy"

          if threshold_reached == 1:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low') AND allergen_name = '%s'""" % key)
          if threshold_reached == 2:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium') AND allergen_name = '%s'""" % key)
          if threshold_reached == 3:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy') AND allergen_name = '%s'""" % key)
          if threshold_reached == 4:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy','extremely heavy') AND allergen_name = '%s'""" % key)
          res = cursor.fetchall()
          if len(res) > 0:
            res[0]["reached"] = reached
            res_all=res_all+res

        for key in weed_keys:
          threshold_reached = 0
          reached = "None"
          for i in range(len(results)):
              if results[i]['allergen_name'] == key:  
                threshold_num=results[i]['count']
                if results[i]['count'] > 0:
                  threshold_reached = 1
                  reached = "low"
                if results[i]['count'] > 4:
                  threshold_reached = 2
                  reached = "medium"
                if results[i]['count'] > 19:
                  threshold_reached = 3
                  reached = "heavy"
                if results[i]['count'] > 200:
                  threshold_reached=4
                  reached = "extremely heavy"
          if threshold_reached == 1:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low') AND allergen_name = '%s'""" % key)
          if threshold_reached == 2:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium') AND allergen_name = '%s'""" % key)
          if threshold_reached == 3:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy') AND allergen_name = '%s'""" % key)
          if threshold_reached == 4:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy','extremely heavy') AND allergen_name = '%s'""" % key)
          res = cursor.fetchall()
          if len(res) > 0:
            res[0]["reached"] = reached
            res_all = res_all + res

        for key in mold_keys:
          threshold_reached=0
          reached = "None"
          for i in range(len(results)):
              if results[i]['allergen_name']==key:  
                threshold_num=results[i]['count']
                if results[i]['count']>0:
                  threshold_reached=1
                  reached = "low"
                if results[i]['count']>6499:
                  threshold_reached=2
                  reached = "medium"
                if results[i]['count']>12999:
                  threshold_reached=3
                  reached = "heavy"
                if results[i]['count']>49999:
                  threshold_reached=4
                  reached = "extremely heavy"
          if threshold_reached==1:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low') AND allergen_name = '%s'""" % key)
          if threshold_reached==2:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium') AND allergen_name = '%s'""" % key)
          if threshold_reached==3:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy') AND allergen_name = '%s'""" % key)
          if threshold_reached==4:
            cursor.execute("""select * from subscriptions WHERE threshold IN ('low','medium','heavy','extreme') AND allergen_name = '%s'""" % key)
          res=cursor.fetchall()
          if len(res)>0:
            res[0]["reached"] = reached
            res_all=res_all+res

        unique_user=set()
        for res in res_all:
            if res['user_id'] not in unique_user:
                unique_user.add(res['user_id'])

        for user in unique_user:
            alerts_user=[]
            for res in res_all:
               if res['user_id']==user:
                    print(res)
                    alerts_user.append(res['allergen_name'])
            print("alert user ",user," for ", alerts_user)
finally:
    db.close()
