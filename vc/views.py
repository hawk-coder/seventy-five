from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator
from django.utils.text import slugify
# Create your views here.

def post_list(request):
	posts = Post.objects.all()

	reverseOut = Post.objects.order_by('-datepub')

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	
	context= {
		'posts': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url,
		'reverseOut': reverseOut
	}

	return render(request, 'vc/index.html', context = context)


def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'vc/post_detail.html', context={'post' : post})