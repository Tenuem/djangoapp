from django.shortcuts import render

# Create your views here.
# myapp/views.py

# artisticapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Post

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            print("nieudana rejestracja")
    else:
        form = CustomUserCreationForm()
    return render(request, 'artisticapp/register.html', {'form': form})


from django.shortcuts import redirect
from django.urls import reverse
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
    else:
        form = CustomAuthenticationForm()
    return render(request, 'artisticapp/login.html', {'form': form})

def home(request):
    if request.method == "POST":
        print("logout correctly")
    posts = Post.objects.all()
    return render(request, 'artisticapp/home.html', {'posts': posts})

def add_post(request):
    if request.user.is_authenticated is False:
        return redirect('login')
    if request.user.is_editor is False:
        return redirect('home')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect('/')
    return render(request, 'artisticapp/add_post.html')

from .forms import CommentForm
from django.shortcuts import get_object_or_404
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'artisticapp/post_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })