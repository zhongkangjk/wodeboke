from django.views.generic import ListView
from .models import Urlclass

class indexListView(ListView):
    # 上下文的名称
    context_object_name = 'urls'
    # 查询集
    queryset = Urlclass.objects.all()
    # 模板位置
    template_name = '收藏夹/收藏夹列表.html'