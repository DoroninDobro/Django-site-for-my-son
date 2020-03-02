import datetime
from django.db import models

from django.utils import timezone

# Create your models here.
class Article(models.Model):
    article_title = models.CharField('Name of Article', max_length=200)
    image = models.FileField(null=True, blank=True)
    article_test = models.TextField('Body of Article')
    pub_date = models.DateTimeField('Date of Publication')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
        

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Comment's Author", max_length=50)
    comment_text = models.CharField("Comment's Body", max_length=200)

    def __str__(self):
        return self.author_name