from django.contrib import admin
from .models import Category, Comment, Author, Post, Subscriber


def delete_all_news(modeladmin, request, queryset):
    Post.objects.all().delete() # удаляем все статьи


def delete_all_ratings(modeladmin, request, queryset):
    Post.objects.all().update(rating=0) # обнуляем рейтинг


def delete_all_comments(modeladmin, request, queryset):
    Comment.objects.all().delete() # удаляем все комментарии


class PostCategoryFilter(admin.SimpleListFilter):
    title = ('Category')
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        categories = set() # создаём множество
        for post in model_admin.get_queryset(request):
            categories.update(post.category.all())  # добавляем к множеству все категории
        return [(category.id, str(category)) for category in categories] # возвращаем множество в виде кортежа

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(category__id=value) # фильтра по категории
        return queryset


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('author', 'title', 'text', 'post_category_display', 'category_type', 'rating') # определяем, какие поля отображать в админке
#     list_filter = ('category_type', 'author', 'data_creation', PostCategoryFilter) # определяем фильтры
#     search_fields = ('title', 'text') # определяем по каким полям искать
#     actions = [delete_all_news, delete_all_ratings] # определяем действия, которые можно совершить
#
#     def post_category_display(self, obj):
#         return ', '.join([category.title for category in obj.category.all()]) # возвращаем все категории
#
#     post_category_display.short_description = 'Category'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'rating_author')
    list_filter = ('nickname', 'rating_author')
    search_fields = ('nickname', 'rating_author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_user', 'comment_post', 'text')
    list_filter = ('comment_post', 'comment_user')
    search_fields = ('comment_user', 'comment_post')
    actions = [delete_all_comments]


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'category')
    list_filter = ('category', 'user')
    search_fields = ('user', 'category')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscriber, SubscriberAdmin)

