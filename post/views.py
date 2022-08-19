from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost
from django.core.paginator import Paginator

# postcreate
def postcreate(request):
    # request method가 post일 경우
    # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # request method가 get일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'postForm.html', {'form': form})
# 게시글 전체
def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5) #5개 단위로 페이지를 끊어줄꺼다
    pagnum = request.GET.get('page') #딕셔너리 형태로 담겨있음, 페이지에 매칭되는 숫자를 가져와라
    posts = paginator.get_page(pagnum)
    return render(request, 'post/home.html', {'posts':posts})

#### 자유게시판
def freeposts(request):
    posts = Post.objects.get(po_category = '자유게시판')
    return render(request, 'post/freePostList.html', {'posts':posts})

#### 후기게시판
def reviewposts(request):
    posts = Post.objects.get(po_category = '후기')
    return render(request, 'post/reviewPostList.html', {'posts':posts})

#### 함께해요 게시판
def withposts(request):
    posts = Post.objects.get(po_category = '같이가요&해요')
    return render(request, 'post/withPostList.html', {'posts':posts})

################################
'''
def postcreate(request):
    # request method가 post일 경우
    # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    # request method가 get일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

# 상세보기
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글을 저장해줌
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) # 어떤 post의 댓글인지 모르니 아직은 저장하지 말고 기다려
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save() # 저장해~
    return redirect('detail', post_id)



####### 자유게시판 ######################

def freehome(request):
    freeposts = FreePost.objects.all()
    return render(request, 'free_index.html', {'freeposts': freeposts})

def freepostcreate(request):
    # request method가 post일 경우 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user #작성자 추가
            unfinished.save()
            return redirect('freehome')

    # request method가 get일 경우 form 입력 html 띄우기
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form': form})

# 상세보기
def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글을 저장해줌
def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) # 어떤 post의 댓글인지 모르니 아직은 저장하지 말고 기다려
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save() # 저장해~
    return redirect('freedetail', post_id)
'''