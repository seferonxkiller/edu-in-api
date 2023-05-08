from django.contrib import admin
from .models import Category, Tag, Subscribe, FAQ, Question, Contact
from modeltranslation.admin import TranslationAdmin

#
# @admin.register(Category)
# class CategoryAdmin(TranslationAdmin):
#     list_display = ('id', 'title')
#     search_fields = ('title', )
#
#
# @admin.register(Tag)
# class TagAdmin(TranslationAdmin):
#     list_display = ('id', 'title')
#     search_fields = ('title', )
#
#
# @admin.register(Subscribe)
# class SubscribeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email')
#     search_fields = ('email', )
#
#
# class AnswerInline(admin.TabularInline):
#     model = Question
#     extra = 1
#
#
# @admin.register(FAQ)
# class FAQAdmin(admin.ModelAdmin):
#     inlines = (AnswerInline, )
#     list_display = ('id', 'question')
#     search_fields = ('question', )
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Subscribe)
admin.site.register(FAQ)
admin.site.register(Question)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_date')
    search_fields = ('name', 'email')
    date_hierarchy = 'created_date'



