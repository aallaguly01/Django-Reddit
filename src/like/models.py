from django.db import models

# Create your models here.
from src.account.models import Account
from src.blog.models import BlogPost


class Like(models.Model):
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models)
    count = models.IntegerField(default=0)