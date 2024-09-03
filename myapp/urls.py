from django.urls import path, re_path

from . import views

urlpatterns = [
    # render加载模板函数
    path('', views.index, name = "index"),
    path('info',views.inFo, name = "info"),
    path('dis_index',views.dis_index, name = "dis_index"),
    path('misdiagnose_web', views.misDiagnoseWeb, name = "misdiagnose_web"),
    path('news',views.news, name = "news"),

    # 测试
    path('test', views.test, name = "test"),

    # 模板
    path('bar_race',views.bar_race, name = "bar_race"),
    path('dis_info',views.dis_info, name = "dis_info"),
    path('cluster',views.cluster, name = "cluster"),
    path('wordcloud',views.wordcloud, name = "wordcloud"),
    path('linechart',views.linechart, name = "linechart"),
    path('SectorGraph',views.SectorGraph, name = "SectorGraph"),

    # JsonResponse获取路径函数
    path('news_info',views.news_info, name = "news_info"),
    path('check',views.check, name = "check"),

    # 备用
    path('files', views.files, name = "files"),

    # 保留
    path('by_misdiagnose_web',views.by_misdiagnose_web, name = "by_misdiagnose_web"),
]