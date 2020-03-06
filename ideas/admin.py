from django.contrib import admin
from .models import Idea, Submission
from django.template.defaultfilters import slugify

# Register your models here.

class IdeaAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'created_at', 'slug', 'author']
    readonly_fields = ['created_at', 'author']
    list_display = ('title', 'description', 'created_at', 'author')

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        if not obj.slug:
            obj.slug = slugify(obj.title)
        obj.save()


class SubmissionAdmin(admin.ModelAdmin):
    fields = ['idea', 'url_to', 'author']
    readonly_fields = ['author', 'id']

    list_display = ('id','idea', 'url_to', 'author')
    list_display_links = ('id', 'idea')

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

admin.site.register(Idea, IdeaAdmin)
admin.site.register(Submission, SubmissionAdmin)