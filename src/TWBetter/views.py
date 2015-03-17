# -*- coding:utf-8 -*-

import json
import operator

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

from DBProj import settings
from TWBetter.models import Producer, GFood, UserProfile, Favorite


# Create your views here.
def welcome(request):
    county_dict = {1:"台北", 2:"桃園", 3:"新竹", 4:"苗栗", 5:"台中", 6:"彰化", 7:"雲林", 8:"嘉義", 9:"台南", 10:"高雄", 11:"屏東", 12:"澎湖"}
    request.session["county_dict"] = county_dict
    
    return render(request, 'home.html', {"county_dict":county_dict})

def query_info(request):
    if request.method == "POST":
        selects = [x.encode("utf-8") for x in request.POST.getlist("county")]
        print "---收到內容---"
        print selects
        print "--- Session內容---"
        for key in request.session["county_dict"].keys():
            value = request.session["county_dict"][key].encode("utf-8")
            print "鍵值:", str(key), ";值:", str(value)
        val_list = []
        for s in selects:
            value = request.session["county_dict"][s].encode("utf-8")
            val_list.append(value)
        print "--- query內容---"
        for v in val_list:
            print v
        result = GFood.objects.filter(reduce(operator.or_, (Q(producer__address__contains=x) for x in val_list)))
        print "--- query結果---"
        for r in result:
            print r.key, ";", r.title, ";", r.producer.address
        
        return render(request, 'result.html', {"result":result})

def detail(request, id):
    id = id.encode("utf-8")
    gfood = GFood.objects.get(pk=int(id))
    is_edited = ""
    account_value = ""
    email_value = ""
    nickname_value = ""
    print "鍵值:", gfood.key, ";名稱:", gfood.title, ";地址:", gfood.producer.address
    return render(request, "detail.html", locals())

def add_favorite(request, id):
    result_message = "存取失敗，請重試或登入"
    status = "0"
                
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user_background=request.user)
        gfood = GFood.objects.get(pk=int(id))
        #exist
        if len(list(Favorite.objects.filter(Q(user_profile=user_profile) & Q(gfood=gfood)))) > 0:
            result_message = "已在追蹤清單"
            status = "1"
            data = {"result_message": result_message, "status": status}
            return HttpResponse(json.dumps(data), content_type="application/json")            
        f = Favorite(user_profile=user_profile, gfood=gfood)
        f.save()
        
        try:
            if len(list(Favorite.objects.filter(Q(user_profile=user_profile) & Q(gfood=gfood)))) > 0:
                favorite_list = list(Favorite.objects.filter(user_profile=user_profile))
                for f in favorite_list:
                    print f.user_profile.user_background.username
                    print f.gfood.title
                result_message = "已加入追蹤清單"
                status = "1"
            else:
                result_message = "存取失敗，請重試"
                status = "0"                         
        except Favorite.DoesNotExist:
            result_message = "存取失敗，請重試"
            status = "0"
        finally:
            data = {"result_message": result_message, "status": status}
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        HttpResponseRedirect("welcome.html")
                    
def register(request):
    if request.method == "POST" and request.is_ajax():
        account_value = request.POST["name"].encode("utf-8")
        email_value = request.POST["email"].encode("utf-8")
        password_value = request.POST["password"].encode("utf-8")
        account_value = str(account_value).strip().strip(" ").strip("\n")
        email_value = str(email_value).strip().strip(" ").strip("\n")
        password_value = str(password_value).strip().strip(" ").strip("\n")
        
        result_message = ""
        status = ""
        try:
            result_user = User.objects.get(username=account_value)
            result_message = "已存在的帳號，請登入"
            status = "0"
        except User.DoesNotExist:
            user = User.objects.create_user(account_value, email_value, password_value)
            user.save()
            u = UserProfile(user_background=user, user_membership=True)
            u.save()
            if u:
                result_message = "新增成功"
                status = "1"
            else:
                result_message = "新增失敗"
                status = "0"
                print "結果:", result_message, ";帳號:", u.user_background.username
        
        data = {"result_message": result_message, "status": status}
        
    return HttpResponse(json.dumps(data), content_type="application/json")

def user_login(request):
    if request.method == "POST" and request.is_ajax():
        username = request.POST["name"].encode("utf-8")
        password = request.POST["password"].encode("utf-8")
        username = str(username).strip().strip(" ").strip("\n")
        password = str(password).strip().strip(" ").strip("\n")
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                print "登入成功!"
                return HttpResponse(json.dumps({"result_message":"登入成功", "status": "1"}), content_type="application/json")
            else:
                print "重導首頁"
                return HttpResponseRedirect('/welcome/')
        else:
            print "錯誤的帳號或密碼!"
            return HttpResponse(json.dumps({"result_message":"錯誤的帳號或密碼", "status": "0"}), content_type="application/json")

@login_required        
def user_logout(request):
    result_message = ""
    status = ""
    
    if request.is_ajax():
        try:
            logout(request)
            del request.session["favorite_list"]
            request.session["favorite_list"]= []
            status = "1"
            result_message = "登出成功"
        except:
            status = "0"
            result_message = "登出失敗"
        
    data = {"result_message": result_message, "status": status}
    return HttpResponse(json.dumps(data), content_type="application/json")

def display_favorite(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user_background=request.user)
        favorite_list = list(Favorite.objects.filter(user_profile=user_profile))
        return render(request, 'favorite.html', {"favorite_list":favorite_list})
    else:
        return HttpResponseRedirect("welcome.html")
            