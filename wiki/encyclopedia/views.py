import re
from django.shortcuts import render
from markdown2 import Markdown
from random import randint
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):  
    if title.lower() in [entry.lower() for entry in util.list_entries()]:        
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": Markdown().convert(util.get_entry(title))
        })    
    else:
        return render(request, "encyclopedia/error404.html", {
            "title": title
        })

def search(request):
    query = request.POST['q']        
    if query.lower() in [entry.lower() for entry in util.list_entries()]:
        return entry(request, query)
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": [entry for entry in util.list_entries() if query.lower() in entry.lower()]
    })

def create(request, duplicate=False):
    if not duplicate:
        return render(request, "encyclopedia/create.html", {
            'duplicate': False
        })
    return render(request, "encyclopedia/create.html", {
        'duplicate': True,
        'article_title': request.POST['article_title'],
        'article_content': request.POST['article_content'],
    })

def edit(request, title):
    return render(request, "encyclopedia/edit.html", {
        'title': title,
        "content": util.get_entry(title)
    })

def save(request):    
    title, content = request.POST['article_title'], request.POST['article_content']
    if title.lower() in [entry.lower() for entry in util.list_entries()] and "updating" not in request.POST:
        return create(request, duplicate=True)
    util.save_entry(title, content)    
    return entry(request, title)

def random(request):
    randomTitle = util.list_entries()[randint(0, len(util.list_entries()) - 1)]
    return render(request, "encyclopedia/entry.html", {
        "title": randomTitle,
        "content": Markdown().convert(util.get_entry(randomTitle))
    }) 