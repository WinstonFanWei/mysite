from django.db import models
from datetime import datetime

# db_table = "news_data"  # 指定真实表名
# Create your models here.

class News(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    ID = models.IntegerField()
    title = models.TextField()
    web_site = models.TextField()
    image_src = models.TextField()
    text = models.TextField()
    source = models.TextField()
    show_time = models.TextField()

    class Meta:
        db_table = "news"

class Artnum_Country(models.Model):
    ID = models.IntegerField()
    article_num = models.IntegerField()
    year = models.TextField()
    country = models.TextField()