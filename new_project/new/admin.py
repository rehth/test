from django.contrib import admin
from new.models import Goods
# Register your models here.


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_info']


