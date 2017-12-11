from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post,Comment
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import PostForm,CommentForm
from websocket import create_connection
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def blog_list(request):
	post = Post.objects.all()
	return render(request,'blogapp/blog_list.html',{'posts':post})

def blog_detail(request,post_id):
	post = get_object_or_404(Post,id=post_id)
	comments =post.comment_set.all()
	form = CommentForm()
	return render(request,'blogapp/post.html',{'post':post,'comments':comments,'form':form})

@login_required(login_url='/blog/log_in')
def comment(request,post_id):
	if request.method == 'POST':
		post = get_object_or_404(Post,id=post_id)
		form = CommentForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			comment = Comment(content = content,owner = request.user , post_ref = post)
			comment.save()
		return redirect(reverse('blogapp:blog_detail',args=[post_id]))

@login_required(login_url='/blog/log_in')
def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			content =  form.cleaned_data['content']
			subject =  form.cleaned_data['subject']
			post = Post(subject = subject,content = content,owner = request.user)
			post.save()
			ws = create_connection("ws://localhost:8000/blog_list/")
			ws.send(json.dumps({'post_id':post.id,'subject':post.subject,'content':post.content}))
			ws.close()
			return redirect(reverse('blogapp:blog_detail',args=[post.id]))
	else:
		form = PostForm()
	return render(request,'blogapp/new_post.html',{'form':form})

@login_required(login_url='/blog/log_in')
def edit_post(request,post_id):
	# Chech if post_id exists
	post = get_object_or_404(Post,id=post_id)
	# Check Owner 
	owner = post.owner
	if owner == request.user:
		# If method == post
		if request.method == 'POST':
			form = PostForm(request.POST)
			if form.is_valid():
				post = get_object_or_404(Post,id=post_id)
				content =  form.cleaned_data['content']
				subject =  form.cleaned_data['subject']
				post.content = content;
				post.subject = subject
				post.save()
				ws = create_connection("ws://localhost:8000/blog_detail/%s/"%post.id)
				ws.send(json.dumps({'subject':subject,'content':content}))
				ws.close()
				return redirect(reverse('blogapp:blog_detail',args=[post.id]))
		else:
			post = get_object_or_404(Post,id=post_id)
			content = post.content
			subject = post.subject
			form = PostForm(initial={'subject':subject,'content':content,'post_id':post.id})
		return render(request,'blogapp/edit_post.html',{'form':form})
	else:
		return HttpResponse("Not Authorized")

@login_required(login_url='/blog/log_in')
def delete_post(request,post_id):
	# Chech if post_id exists
	post = get_object_or_404(Post,id=post_id)
	# Check Owner 
	owner = post.owner
	if owner == request.user:
		post = get_object_or_404(Post,id=post_id)
		ws = create_connection("ws://localhost:8000/blog_detail/%s/"%post.id)
		post.delete()
		ws.send(json.dumps({'subject':"",'content':""}))
		ws.close()
		return redirect(reverse('blogapp:blog_list'))
	else:
		return HttpResponse("Not Authorized")

def log_in(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect(reverse('blogapp:blog_list'))
		else:
			print(form.errors)
	return render(request, 'blogapp/log_in.html', {'form': form})

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blogapp:log_in'))
        else:
            print(form.errors)
    return render(request, 'blogapp/sign_up.html', {'form': form})


def log_out(request):
	logout(request)
	return redirect(reverse('blogapp:log_in'))
