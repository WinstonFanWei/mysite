from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404,JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from myadmin.models import *
from django.db.models import Q
import os
import sys

#render加载模板函数

def myadmin_index(request):
    adminlist = AdminUsers.objects.all().order_by('userid')
    admin_num = adminlist.__len__()
    Newslist = News.objects.all().order_by('newsID')
    news_num = Newslist.__len__()
    Userlist = Users.objects.all().order_by('userid')
    user_num = Userlist.__len__()
    context = {'admin_num': admin_num, 'news_num': news_num, 'user_num': user_num}
    return render(request, "myadmin/index.html", context)

def myadmin_watchNews(request, pIndex = 1):
    """浏览新闻信息"""
    Newsmod = News.objects
    Newslist = Newsmod.all().order_by('newsID')
    mywhere=[]
    kw = request.GET.get("keyword",None)
    if kw:
        Newslist = Newslist.filter(Q(title__contains=kw) | Q(source__contains=kw))
        mywhere.append('keyword=' + kw)
    pIndex = int(pIndex)
    page = Paginator(Newslist,10)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range
    context = {"newslist":list2, 'plist':plist, 'pIndex':pIndex, 'maxpages':maxpages, 'mywhere':mywhere}
    return render(request, "myadmin/Newslist.html", context)

def myadmin_addNews(request):
    """加载信息添加表单"""
    return render(request, "myadmin/add.html")

def myadmin_insert(request):
    Newsmod = News.objects
    Newslist = Newsmod.all()
    """执行信息添加"""
    try:
        ob = News()
        i = 0
        for news in Newslist:
            if news.newsID > i:
                i = news.id
        ob.newsID = i + 1
        ob.id = i + 1
        ob.title = request.POST['title']
        ob.web_site = request.POST['web_site']
        ob.image_src = request.POST['image_src']
        ob.text = request.POST['text']
        ob.source = request.POST['source']
        ob.show_time = request.POST['show_time']
        ob.save()
        context = {'info':"添加成功! "}
    except Exception as err:
        print(err)
        context = {'info':"添加失败! ", 'err':err}
    return render(request, "myadmin/info.html", context)

def myadmin_edit(request, ID=0):
    """加载信息修改表单"""
    try:
        ob = News.objects.get(newsID=ID)
        context = {'news': ob}
        return render(request, "myadmin/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息! "}
        return render(request, "myadmin/info.html", context)

def myadmin_update(request, ID=0):
    """执行信息修改"""
    try:
        ob = News.objects.get(newsID=ID)
        ob.title = request.POST['title']
        ob.web_site = request.POST['web_site']
        ob.image_src = request.POST['image_src']
        ob.text = request.POST['text']
        ob.source = request.POST['source']
        ob.show_time = request.POST['show_time']
        ob.save()
        context ={'info': "修改成功! "}
    except Exception as err:
        print(err)
        context = {'info': "修改失败! "}
    return render(request, "myadmin/info.html", context)

def myadmin_login(request):
    return render(request, "myadmin/login.html")

def myadmin_sign(request):
    return render(request, "myadmin/sign.html")

def myadmin_dologin(request):
    if request.POST['user_type'] == 'admin':
        try:
            adminuser = AdminUsers.objects.get(username = request.POST['username'])
            _pw = request.POST['password']
            if(adminuser.password == _pw):
                request.session['adminuser'] = adminuser.toDict()
                return redirect(reverse("myadmin_index"))
            else:
                context = {'info':"密码错误!(三次后锁定)"}
        except Exception as err:
            context = {"info":"账号不存在!"}
        return render(request, "myadmin/login.html", context)
    else:
        try:
            user = Users.objects.get(username = request.POST['username'])
            _pw = request.POST['password']
            if(user.password == _pw):
                request.session['adminuser'] = user.toDict()
                return redirect(reverse("index")+"?uname="+request.POST['username'])
            else:
                context = {'info':"密码错误!(三次后锁定)"}
        except Exception as err:
            context = {"info":"账号不存在!"}
        return render(request, "myadmin/login.html", context)

def myadmin_dosign(request):
    if request.POST['password'] != request.POST['_password']:
        context = {'info':"两次密码输入不一致! "}
        return render(request, "myadmin/sign.html", context)
    userlist = Users.objects.all()
    i = 0
    for user in userlist:
        if user.userid > i:
            i = user.userid
        if user.username == request.POST['username']:
            context = {'info':"账号已存在! "}
            return render(request, "myadmin/sign.html", context)
    """执行信息添加"""
    try:
        ob = Users()
        ob.userid = i
        ob.username = request.POST['username']
        ob.password = request.POST['password']
        ob.tele = request.POST['tele']
        ob.email = request.POST['email']
        ob.save()
        context = {'info':"注册成功! "}
    except Exception as err:
        print(err)
        context = {'info':"注册失败! "}
    return render(request, "myadmin/sign.html", context)

def myadmin_logout(request):
    del request.session['adminuser']
    return redirect(reverse("myadmin_login"))

def myadmin_watchAdmins(request, pIndex = 1):
    """浏览员工信息"""
    Adminmod = AdminUsers.objects
    Adminlist = Adminmod.all().order_by('userid')
    mywhere=[]
    kw = request.GET.get("keyword",None)
    if kw:
        Adminlist = Adminlist.filter(Q(username__contains=kw) | Q(tele__contains=kw))
        mywhere.append('keyword=' + kw)
    pIndex = int(pIndex)
    page = Paginator(Adminlist,10)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range
    context = {"Adminlist":list2, 'plist':plist, 'pIndex':pIndex, 'maxpages':maxpages, 'mywhere':mywhere}
    return render(request, "myadmin/Adminlist.html", context)

def myadmin_addAdmin(request):
    """加载信息添加表单"""
    return render(request, "myadmin/addAdmin.html")

def myadmin_insertAdmin(request):
    Adminmod = AdminUsers.objects
    Adminlist = Adminmod.all()
    """执行信息添加"""
    try:
        ob = AdminUsers()
        i = 0
        for admin in Adminlist:
            if admin.userid > i:
                i = admin.userid
        ob.userid = i + 1
        ob.id = i + 1
        ob.username = request.POST['username']
        ob.tele = request.POST['tele']
        ob.email = request.POST['email']
        ob.userinfo = request.POST['userinfo']
        ob.password = request.POST['password']
        ob.save()
        context = {'info':"添加成功! "}
    except Exception as err:
        print(err)
        context = {'info':"添加失败! ", 'err':err}
    return render(request, "myadmin/admininfo.html", context)

def myadmin_editAdmin(request, ID=0):
    """加载信息修改表单"""
    try:
        ob = AdminUsers.objects.get(userid=ID)
        context = {'admin': ob}
        return render(request, "myadmin/editAdmin.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息! ", 'err':err}
        return render(request, "myadmin/admininfo.html", context)

def myadmin_updateAdmin(request, ID=0):
    """执行信息修改"""
    try:
        ob = AdminUsers.objects.get(userid=ID)
        ob.username = request.POST['username']
        ob.tele = request.POST['tele']
        ob.email = request.POST['email']
        ob.userinfo = request.POST['userinfo']
        ob.password = request.POST['password']
        ob.save()
        context ={'info': "修改成功! "}
    except Exception as err:
        print(err)
        context = {'info': "修改失败! "}
    return render(request, "myadmin/admininfo.html", context)

def myadmin_watchUsers(request, pIndex = 1):
    """浏览员工信息"""
    Usermod = Users.objects
    Userlist = Usermod.all().order_by('userid')
    mywhere=[]
    kw = request.GET.get("keyword",None)
    if kw:
        Userlist = Userlist.filter(Q(username__contains=kw) | Q(tele__contains=kw))
        mywhere.append('keyword=' + kw)
    pIndex = int(pIndex)
    page = Paginator(Userlist,10)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range
    context = {"Userlist":list2, 'plist':plist, 'pIndex':pIndex, 'maxpages':maxpages, 'mywhere':mywhere}
    return render(request, "myadmin/Userlist.html", context)

def myadmin_addUser(request):
    """加载信息添加表单"""
    return render(request, "myadmin/addUser.html")

def myadmin_insertUser(request):
    Usermod = Users.objects
    Userlist = Usermod.all()
    """执行信息添加"""
    try:
        ob = Users()
        i = 0
        for user in Userlist:
            if user.userid > i:
                i = user.userid
        ob.userid = i + 1
        ob.id = i + 1
        ob.username = request.POST['username']
        ob.tele = request.POST['tele']
        ob.email = request.POST['email']
        ob.userinfo = request.POST['userinfo']
        ob.password = request.POST['password']
        ob.save()
        context = {'info':"添加成功! "}
    except Exception as err:
        print(err)
        context = {'info':"添加失败! ", 'err':err}
    return render(request, "myadmin/userinfo.html", context)

def myadmin_editUser(request, ID=0):
    """加载信息修改表单"""
    try:
        ob = Users.objects.get(userid=ID)
        context = {'user': ob}
        return render(request, "myadmin/editUser.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息! ", 'err':err}
        return render(request, "myadmin/userinfo.html", context)

def myadmin_updateUser(request, ID=0):
    """执行信息修改"""
    try:
        ob = Users.objects.get(userid=ID)
        ob.username = request.POST['username']
        ob.tele = request.POST['tele']
        ob.email = request.POST['email']
        ob.userinfo = request.POST['userinfo']
        ob.password = request.POST['password']
        ob.save()
        context ={'info': "修改成功! "}
    except Exception as err:
        print(err)
        context = {'info': "修改失败! "}
    return render(request, "myadmin/userinfo.html", context)