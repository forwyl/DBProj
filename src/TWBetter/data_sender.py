# -*- coding:utf-8 -*-
import json
import operator

import django
from django.contrib.auth.models import User
from django.db.models import Q

from TWBetter.models import Producer, GFood, UserProfile, Favorite


django.setup()

def test_query():

    #Delete all first
#     Favorite.objects.all().delete()
#     gfood = GFood.objects.get(pk=5127)
#     print gfood.title, ";", gfood.unit_price, ";", gfood.producer.address
#     u = User.objects.get(username="sgnus")
#     user_profile = UserProfile.objects.get(user_background=u)
#     f = Favorite(user_profile=user_profile, gfood=gfood)
#     f.save()
#     if list(Favorite.objects.filter(Q(user_profile=user_profile) & Q(gfood=gfood) )) > 0:
#         favorite_list = list(Favorite.objects.filter(user_profile=user_profile))
#         for f in favorite_list:
#             print f.user_profile.user_background.username, ";", f.gfood.key

    print "---GFood資料庫資料---" 
    count_dict = {}
    for g in GFood.objects.all():
        if g.producer is not None:
#             print "名稱:", g.title
            for s in list(g.title):
               s = str(s.encode("utf-8")).strip().strip(" ")
               if count_dict.has_key(s):
                   count_dict[s] += 1
               else:
                   count_dict[s] = 1
        else:
            print "編號:", str(g.key) ,";ID:", g.id
        
    count_list = sorted(count_dict.items(), key=operator.itemgetter(1))
    sublist = count_list[-60:]
    for c in sublist:
        print "值:", str(c[0]), "次數:", str(c[1])
            
def insert_GFood():
    data = set()
    f = open("../../dataset/good_food.json")
    line = f.readline() # Invokes readline() method on file
    while line:
        load = json.loads(line.replace("\r\n", ""), strict=False, encoding="UTF-8")
        for i in load:
            type = str(i["type"].encode("UTF-8")).strip().strip(" ").strip("\n")
            agrospec = str(i["agrospec"].encode("UTF-8")).strip().strip(" ").strip("\n")
            catalogs_id = str(i["catalogs_id"].encode("UTF-8")).strip().strip(" ").strip("\n")
            county = str(i["county"].encode("UTF-8")).strip().strip(" ").strip("\n")
            description = str(i["Description"].encode("UTF-8")).strip().strip(" ").strip("\n")
            id = str(i["id"].encode("UTF-8")).strip().strip(" ").strip("\n")
            image_url = str(i["ImageUrl"].encode("UTF-8")).strip().strip(" ").strip("\n")
            link = str(i["link"].encode("UTF-8")).strip().strip(" ").strip("\n")
            spc_catalogs_id = str(i["spc_catalogs_id"].encode("UTF-8")).strip().strip(" ").strip("\n")
            title = str(i["title"].encode("UTF-8")).strip().strip(" ").strip("\n")
            unit_price = str(i["unit_price"].encode("UTF-8")).strip().strip(" ").strip("\n")
            modify_date = str(i["modify_date"].encode("UTF-8")).strip().strip(" ").strip("\n")
            address = str(i["producer_location"].encode("UTF-8")).strip().strip(" ").strip("\n")
            phone = str(i["phone"].encode("UTF-8")).strip().strip(" ").strip("\n")
            producer = None;
#             print "地址:", address, "電話:", phone
#             if len(address) > 0 and len(phone) > 0:
#                 producer = Producer.objects.get(address=address, phone=phone)                
#             else:
#                 if len(address) > 0: producer = Producer.objects.get(address=address)
#                 elif len(phone) > 0: producer = Producer.objects.get(phone=phone)
            if len(address) > 0 or len(phone) > 0:           
                producer = Producer.objects.get(address=address, phone=phone)
            data.add((type, agrospec, catalogs_id, county, description, id, image_url, link, spc_catalogs_id, title, unit_price, modify_date, producer))            
        line = f.readline()
    f.close()
   
   #============================================================================
   # #debug block 
   #  outline = ""
   #  for t in data:  
   #      for i, value in enumerate(t):
   #          if i == 4:
   #              outline += str(value) + ";"
   #          if i == len(t)-1:
   #              if value is not None:
   #                  outline += str(value.key)
   #              else:
   #                  outline += "."
   #      print outline
   #      outline = ""
   #============================================================================
    
    #Delete all first
    while GFood.objects.count():
        ids = GFood.objects.values_list('pk', flat=True)[:100]
        GFood.objects.filter(pk__in = ids).delete()    
    
    for (type, agrospec, catalogs_id, county, description, id, image_url, link, spc_catalogs_id, title, unit_price, modify_date, producer) in data:
        g = GFood(type=type, agrospec=agrospec, catalogs_id=catalogs_id, county=county, description=description, id=id, \
        image_url=image_url, link=link, spc_catalogs_id=spc_catalogs_id, title=title, unit_price=unit_price, \
        modify_date=modify_date, producer=producer)
#         g.save()

    print "---GFood資料庫資料---" 
    for g in GFood.objects.all():
        if g.producer is not None:
            print "編號:", str(g.key) ,";ID:", g.id, ";電話:", str(g.producer.phone.encode("UTF-8")), ";地址:", str(g.producer.address.encode("UTF-8"))
        else:
            print "編號:", str(g.key) ,";ID:", g.id
            
def insert_producer():
    data = set()
    f = open("../../dataset/good_food.json")
    line = f.readline() # Invokes readline() method on file
    while line:
        load = json.loads(line.replace("\r\n", ""), strict=False, encoding="UTF-8")
        for i in load:
            address = str(i["producer_location"].encode("UTF-8")).strip().strip(" ").strip("\n")
            phone = str(i["phone"].encode("UTF-8")).strip().strip(" ").strip("\n")
            data.add((address, phone))
        line = f.readline()
    f.close()
    
    #Delete all first
    while Producer.objects.count():
        ids = Producer.objects.values_list('pk', flat=True)[:100]
        Producer.objects.filter(pk__in = ids).delete()
    
    for address, phone in data:
        print "地址:", address, "電話:", phone
        if len(address) > 0 or len(phone) > 0:
            p = Producer(number="", name="", manager="", address=address, phone=phone, fax="", type=None, website="")
#             p.save()
    
    print "---資料庫資料---" 
    for p in Producer.objects.all():
        print "編號:", str(p.key) ,"地址:", p.address, "電話:", p.phone

# insert_producer()        
# insert_GFood()
test_query()    
    