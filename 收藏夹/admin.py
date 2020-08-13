from django.contrib import admin
from 收藏夹.models import Urlclass

admin.site.site_header = '后台_header'
admin.site.site_title = '后台_title'
admin.site.register(Urlclass)