import datetime
from haystack import indexes
from techBlog.models import Post

class PostIndex(indexes.SearchIndex,indexes.Indexable):
	text = indexes.CharField(document = True, use_template = True)
	title = indexes.Charfield(model_attr = 'title')
	description = indexes.Charfield(model_attr = 'description')
	created = indexes.Charfield(model_attr='created')

	def get_model(self):
		return (Post)

	def index_queryset(self,using=None):
		return self.get_model().objects.filter(created__lte = datetime.datetime.now() )
