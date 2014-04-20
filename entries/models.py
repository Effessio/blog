# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    tag_text = models.CharField(max_length=150, verbose_name=u'Текст тега')

    def __unicode__(self):
            return self.tag_text

    class Meta():
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'


class Entry(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'Заголовок', help_text=u'Максимум 150 символов')
    text = models.TextField(verbose_name=u'Текст записи')
    created_date = models.DateTimeField(auto_now=True)
    tag_list = models.ManyToManyField(Tag, verbose_name=u'Список тегов')

    def __unicode__(self):
            return self.title

    class Meta():
        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'
        ordering = ['created_date']


class Comment(models.Model):
    entry = models.ForeignKey(Entry, verbose_name=u'Запись')
    comment_text = models.CharField(max_length=150, verbose_name=u'Текст комментария')

    def __unicode__(self):
            if len(self.comment_text) > 10:
                return self.comment_text[0:10]
            else:
                return self.comment_text

    class Meta():
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'




