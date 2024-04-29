from django.contrib import admin
from .models import Author, Tag, Quote
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','date_born','location_born')
    list_filter = ('is_active',)
    search_fields = ('fullname', 'bio')
    actions = ['active', 'deactivate']
    ordering = ['id']

@admin.action(description='Mark selected author as active')
def activate(self, request, queryset):
    queryset.update(is_activate= True)

@admin.action(description='Mark selected author as  not active')
def deactivate(self, request, queryset):
    queryset.update(deactivate=False)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ['id']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_author', 'get_tags', 'created_at')
    list_filter = ('tags', )
    search_fields = ('tags__name', 'author__fullname', 'quote')
    ordering = ['id']
    @admin.display(description='Author')
    def get_author(self, obj):
        return obj.author.fullname  
    @admin.display(description='Tags')
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
        