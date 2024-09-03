from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404,JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from myapp.models import *
import os
import sys

#render加载模板函数

def index(request):
    return render(request, "myapp/index.html")

def inFo(request):
    return render(request, "myapp/info.html")

def dis_index(request):
    return render(request, "myapp/dis_index.html")

def misDiagnoseWeb(request):
    return render(request, "myapp/misdiagnose_web.html")

def news(request):
    return render(request, "myapp/news.html")

# 测试页

def test(request):
    return render(request, "myapp/test.html")

# 模板页

def bar_race(request):
    return render(request,"myapp/bar_race.html")

def dis_info(request):
    return render(request, "myapp/dis_info.html")

def cluster(request):
    return render(request, "myapp/cluster.html")

def wordcloud(request):
    return render(request, "myapp/wordcloud.html")

def linechart(request):
    return render(request, "myapp/linechart.html")

def SectorGraph(request):
    return render(request, "myapp/SectorGraph.html")

# JsonResponse获取数据函数

def news_info(request):
    data = {}
    news = News.objects.all().order_by('-show_time')
    ls = []
    for n in news:
        new = {}
        new["title"] = n.title
        new["web_site"] = n.web_site
        new["image_src"] = n.image_src
        new["text"] = n.text
        new["source"] = n.source
        new["show_time"] = n.show_time
        ls.append(new)
    data["news"] = ls
    return JsonResponse(data)

def check(request):
    artnum = Artnum_Country.objects.all()
    data = {}
    ls = []
    num = 0
    y = 2016
    for i in range(6):
        time = str(int(y + i))
        for art in artnum:
            if str(int(art.year)) == time:
                num = num + art.article_num
        ls.append(num)
    data["data"] = ls
    data["type"] = 'line'
    return JsonResponse(data)

# 备用

def files(request):
    pass

# 保留网页

def by_misdiagnose_web(request):
    return render(request, "remain/by_misdiagnose_web.html")

# def filesOne(request):
#     a,b = file_name("./static/pdf01")
#     context = {}
#     context["name"] = a
#     context["routine"] = b
#     return render(request, "myapp/files_1.html", context)

# def filesTwo(request):
#     a,b = file_name("./static/pdf02")
#     context = {}
#     context["name"] = a
#     context["routine"] = b
#     return render(request, "myapp/files_2.html", context)

# def filesThree(request):
#     a,b = file_name("./static/pdf03")
#     context = {}
#     context["name"] = a
#     context["routine"] = b
#     return render(request, "myapp/files_3.html", context)

# def mapTest(request):
#     artnum = Artnum_Country.objects.all()
#     context = {}
#     data = []
#     num = 0
#     y = 2016
#     for i in range(6):
#         time = str(int(y + i))
#         for art in artnum:
#             if str(int(art.year)) == time:
#                 num = num + art.article_num
#         data.append(str(int(num)))
#     context["data"] = data
#     return render(request, "myapp/map_test.html", context)

# def mappingKnowledge(request, sid=1):
#     context = {}
#     context["sid"] = sid
#     return render(request, "myapp/mapping_knowledge.html", context)

#     name = request.GET['name']
#     if name == '脊髓性肌萎缩症':
#         return redirect(reverse('files_1'))
#     elif name == '纯合子家族性高胆固醇血症':
#         return redirect(reverse('files_2'))
#     elif name == '亨廷顿舞蹈病':
#         return redirect(reverse('files_3'))
