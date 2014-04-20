# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Entry, Tag
from .forms import CommentForm



def initial_data():
    odd_tag = Tag.objects.get(tag_text=u'Нечетный')
    even_tag = Tag.objects.get(tag_text=u'Четный')
    if Entry.objects.count() < 10:
        for i in range(25):
            entry = Entry(title=u'Заголовок тестовой записи '+str(i), text=u'Текст тестовой записи '+str(i))
            entry.save()
            if i%2:
                entry.tag_list.add(odd_tag)
            else:
                entry.tag_list.add(even_tag)
            entry.save()
    return 'done'


def get_context(**kwargs):
    result = {'tag_list': Tag.objects.all()}
    for key, value in kwargs.iteritems():
        result[key] = value

    return result


def index(request):
    entries_list = Entry.objects.all().order_by('-created_date')
    paginator = Paginator(entries_list, 10)
    page = request.GET.get('page')
    try:
        entries_list = paginator.page(page)
    except PageNotAnInteger:
        entries_list = paginator.page(1)
    except EmptyPage:
        entries_list = paginator.page(paginator.num_pages)
    context = get_context(entries_list=entries_list)
    return render(request, 'entries/index.html', {'context': context})


def posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    entries_list = tag.entry_set.all()
    paginator = Paginator(entries_list, 10)
    page = request.GET.get('page')
    try:
        entries_list = paginator.page(page)
    except PageNotAnInteger:
        entries_list = paginator.page(1)
    except EmptyPage:
        entries_list = paginator.page(paginator.num_pages)
    context = get_context(entries_list=entries_list)
    return render(request, 'entries/index.html', {'context': context})


def entry_page(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.entry_id = entry_id
            new_comment.save()
            comments = entry.comment_set.all()
            form = CommentForm()
            context = get_context(entry=entry, comments=comments, form=form)
            return render(request, 'entries/entry.html', {'context': context})
        else:
            if entry.comment_set.count() > 0:
                comments = entry.comment_set.all()
            else:
                comments = [{'comment_text': u'Комментариев еще нет'}]
                form = CommentForm()
            context = get_context(entry=entry, comments=comments, form=form)
            return render(request, 'entries/entry.html', {'context': context})
    else:
        if entry.comment_set.count() > 0:
            comments = entry.comment_set.all()
        else:
            comments = [{'comment_text': u'Комментариев еще нет'}]
        form = CommentForm()
        context = get_context(entry=entry, comments=comments, form=form)
        return render(request, 'entries/entry.html', {'context': context})
