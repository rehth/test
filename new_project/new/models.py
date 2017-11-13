from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Goods(models.Model):
    goods_info = HTMLField(verbose_name='商品详情')

    class Meta:
        db_table = 'goods_info'
        verbose_name = '商品详情表'
        verbose_name_plural = verbose_name
