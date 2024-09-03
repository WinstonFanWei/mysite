from django.db import models
from datetime import datetime

# db_table = "news_data"  # 指定真实表名
# Create your models here.

class News(models.Model):
    # id = models.AutoField(primary_key=True) #主键可省略不写
    newsID = models.IntegerField()
    title = models.TextField()
    web_site = models.TextField()
    image_src = models.TextField()
    text = models.TextField()
    source = models.TextField()
    show_time = models.TextField()

    class Meta:
        db_table = "news"

class AdminUsers(models.Model):
    # id = models.AutoField(primary_key=True) #主键可省略不写
    userid = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    userinfo = models.TextField()
    stuid = models.TextField()
    tele = models.TextField()
    email = models.TextField()

    def toDict(self):
        return {'userid':self.userid, 'username':self.username, 'password':self.password, 'userinfo':self.userinfo, 'stuid':self.stuid, 'tele':self.tele, 'email':self.email}
    class Meta:
        db_table = "AdminUsers"

class Users(models.Model):
    userid = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    userinfo = models.TextField()
    tele = models.TextField()
    email = models.TextField()

    def toDict(self):
        return {'userid':self.userid, 'username':self.username, 'password':self.password, 'userinfo':self.userinfo, 'tele':self.tele, 'email':self.email}
    class Meta:
        db_table = "Users"