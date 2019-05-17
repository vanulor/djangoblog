from django.contrib import admin
from blogging.models import Post, Category


# Register your models here.
class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
