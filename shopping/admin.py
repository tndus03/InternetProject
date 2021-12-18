from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from shopping.models import Post, Category, Make, Comment

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class MakeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Make, MakeAdmin)