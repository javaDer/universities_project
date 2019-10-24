from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


class Universities(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=22, blank=True, default='')
    competent_department = models.CharField(max_length=22, blank=True, default='')
    name = models.CharField(max_length=22, blank=True, default='')
    remake = models.CharField(max_length=22, blank=True, default='')
    school_level = models.CharField(max_length=6, blank=True, default='')
    universities_code = models.CharField(max_length=24, blank=True, default='')
    class Meta:
        ordering = ('create_time',)
