from haystack import indexes
from MyBlogs.models import *


# 注意格式(模型类名+Index)
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    context = indexes.NgramField(model_attr='context')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')
