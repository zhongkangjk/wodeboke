from django.db import models

class Urlclass(models.Model):
    title = models.CharField('标题',max_length=100)
    abstract = models.TextField('摘要')
    url = models.URLField('网址')
    class Meta:
        verbose_name = '收藏的网址'
        verbose_name_plural = "收藏的网址"
        #为了在后台显示中文
    def __str__(self):
        return self.title