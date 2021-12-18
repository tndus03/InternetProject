from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from shopping.models import Post, Category, Make

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class MakeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Make, MakeAdmin)