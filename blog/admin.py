from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):

    # how you want to disaply all of the posts
    list_display = ['id', 'title', 'author', 'updated', 'published']

    # how you want to disaply each post profile (This is what is editable)
    fieldsets = [
        ('Meta Info', {'fields': ['id', 'slug', 'author',  'updated', 'published' ]}),
        ('Content', {'fields': ['title','content']}),
        # (None,               {'fields': ['survey_name']}),
        # ('Date Information', {'fields': ['survey_date']}),
    ]

    # make fields un editable
    readonly_fields = ('id', 'author', 'slug', 'updated', 'published')

    # how you want to disaply all of the posts
    search_fields = ['title', 'content']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)