from django.db import models

class Post(models.Model):
    po_title = models.CharField(max_length=200)
    po_contents = models.TextField(null=True)
    po_time = models.DateTimeField(auto_now_add=True)
    Cate=(
        ('자유게시판','자유게시판'),
        ('후기','후기'),
        ('같이가요&해요', '같이가요&해요')
    )
    po_category = models.CharField(max_length=20, choices=Cate, default='')
    po_user_id = models.CharField(max_length=30)
    po_user_pass = models.CharField(max_length=50)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.po_title

class Comment(models.Model):
    co_contents = models.TextField()
    co_user_id = models.CharField(max_length=30)
    co_user_pass = models.CharField(max_length=50)
    co_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.co_contents
