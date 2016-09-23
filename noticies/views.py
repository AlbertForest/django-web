from django.shortcuts import render
from .models import post

# Create your views here.

def post_list(request):
	noticies = post.objects.order_by('id_post')
	return render(request,'post_list.html',{'noticies':noticies})
