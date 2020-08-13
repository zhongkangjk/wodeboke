#引入path
from django.urls import path
# 引入view.py
from . import views

# 正在部署的应用名称
app_name = 'index'

urlpatterns = [
    # path函数将url映射到视图
    path('',views.indexListView.as_view(),name='收藏夹列表'),

]