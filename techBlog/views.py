from django.shortcuts import render, get_object_or_404, HttpResponse
from techBlog.models import Post

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-created')[1:]
	hero = Post.objects.order_by('-created')[0]
	return render(request,'techBlog/index.html',{'posts' : posts,'hero' : hero})
def trending(request):
	posts = Post.objects.order_by('-views')[:5]
	return render(request,'techBlog/trending.html',{'posts': posts})
def post(request,slug):
	post = get_object_or_404(Post,slug = slug)
	post.views = post.views + 1
	post.save()
	return render(request,'techBlog/post.html',{'post':post})
def search(request):
	q = request.POST['search']
	q = q.split();
	for que in q:
		posts = Post.objects.filter(title__icontains = que).order_by('-created')
	return render(request,'techBlog/search.html',{'posts' : posts, 'query' : q })

	
	

