from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

# Apply summernote to all TextField in model.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

admin.site.register(Post, PostAdmin)


# class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'

# admin.site.register(Post, SomeModelAdmin)


