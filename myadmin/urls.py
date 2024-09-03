from django.urls import path, re_path

from . import views

urlpatterns = [
    # render加载模板函数
    path('', views.myadmin_index, name = "myadmin_index"),

    path('myadmin_watchNews/<int:pIndex>', views.myadmin_watchNews, name = "myadmin_watchNews"),
    path('myadmin_addNews', views.myadmin_addNews, name = "myadmin_addNews"),
    path('myadmin_insert', views.myadmin_insert, name = "myadmin_insert"),
    path('myadmin_edit/<int:ID>', views.myadmin_edit, name = "myadmin_edit"),
    path('myadmin_update/<int:ID>', views.myadmin_update, name = "myadmin_update"),
    
    path('myadmin_login', views.myadmin_login, name = "myadmin_login"),
    path('myadmin_dologin', views.myadmin_dologin, name = "myadmin_dologin"),
    path('myadmin_logout', views.myadmin_logout, name = "myadmin_logout"),
    path('myadmin_sign', views.myadmin_sign, name = "myadmin_sign"),
    path('myadmin_dosign', views.myadmin_dosign, name = "myadmin_dosign"),

    path('myadmin_watchAdmins/<int:pIndex>', views.myadmin_watchAdmins, name = "myadmin_watchAdmins"),
    path('myadmin_addAdmin', views.myadmin_addAdmin, name = "myadmin_addAdmin"),
    path('myadmin_insertAdmin', views.myadmin_insertAdmin, name = "myadmin_insertAdmin"),
    path('myadmin_editAdmin/<int:ID>', views.myadmin_editAdmin, name = "myadmin_editAdmin"),
    path('myadmin_updateAdmin/<int:ID>', views.myadmin_updateAdmin, name = "myadmin_updateAdmin"),

    path('myadmin_watchUsers/<int:pIndex>', views.myadmin_watchUsers, name = "myadmin_watchUsers"),
    path('myadmin_addUser', views.myadmin_addUser, name = "myadmin_addUser"),
    path('myadmin_insertUser', views.myadmin_insertUser, name = "myadmin_insertUser"),
    path('myadmin_editUser/<int:ID>', views.myadmin_editUser, name = "myadmin_editUser"),
    path('myadmin_updateUser/<int:ID>', views.myadmin_updateUser, name = "myadmin_updateUser"),
]