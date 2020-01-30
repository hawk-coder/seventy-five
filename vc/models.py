from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, help_text="Название")
    slug = AutoSlugField(max_length=300, unique=True, populate_from='title' )
    describe_text = models.TextField(max_length=150, blank=True, help_text='Описание которое будет выведенно на главной странице')
    # image = models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d', verbose_name='Ссылка картинки')
    body = models.TextField(db_index=True, blank=True)
    datepub = models.DateTimeField(auto_now_add=True)

   

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    

    def __str__(self):
        return '{}'.format(self.title)
    