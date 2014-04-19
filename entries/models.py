# -*- coding: utf-8 -*-
from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'Заголовок', help_text=u'Максимум 150 символов')
    text = models.TextField(verbose_name=u'Текст записи')
    create_date = models.DateTimeField(auto_now=True)
    tag_list = models.ManyToManyField(Tag, verbose_name=u'Список тегов')

    class Meta():
        verbose_name = u'Запись'
        verbose_names = u'Записи'


class Tag(models.Model):
    tag_text = models.CharField(max_length=150, verbose_name=u'Текст тега')

    class Meta():
        verbose_name = u'Тег'
        verbose_names = u'Теги'


class Comment(models.Model):
    comment_text = models.TextField(verbose_name=u'Текст комментария')
    entry = models.ManyToManyField(Entry, verbose_name=u'Запись')

    class Meta():
        verbose_name = u'Комментарий'
        verbose_name = u'Комментарии'
