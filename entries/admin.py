# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Entry, Tag, Comment


class TagAdmin(admin.ModelAdmin):
    model = Tag


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    fk_name = 'entry'


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('title', 'created_date')
    inlines = [CommentInline]
    search_fields = ('title', 'text')


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)