from django.shortcuts import render
import markdown
import random as rnd

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_markdown(title):
    content = util.get_entry(title)
    markdown2 = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdown2.convert(content)
    
def entry(request, title):
    html_content = convert_markdown(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message":"This entry does not exist"
        })
    else:
        return render(request,"encyclopedia/entry.html",{
            "title":title,
            "content":html_content
        })

def search(request):
    if request.method == "POST":
        form_search = request.POST['q']
        html_content = convert_markdown(form_search)
        if html_content is not None:
            return render(request,"encyclopedia/entry.html",{
            "title":form_search,
            "content":html_content
        })
        else:
            all_entries = util.list_entries()
            advice = []
            for entry in all_entries:
                if form_search.lower() in entry.lower():
                    advice.append(entry)
            return render(request, "encyclopedia/search.html",{
                "advice":advice
            })
        
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exs = util.get_entry(title)
        if title_exs is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "Entry page already exists."
            })
        else:
            util.save_entry(title, content)
            html_content = convert_markdown(title)
            return render(request,"encyclopedia/entry.html", {
                "title" : title,
                "content" :html_content
            })
        
def edit(request):
    if request.method == 'POST':
        edit_title = request.POST['entry_title']
        edit_content = util.get_entry(edit_title)
        return render(request,"encyclopedia/edit.html", {
            "title":edit_title,
            "content":edit_content
        })

def edit_view(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        html_content = convert_markdown(title)
        return render(request,"encyclopedia/entry.html", {
                "title" : title,
                "content" :html_content
            })
    
def random(request):
    all_entries = util.list_entries()
    random_entry = rnd.choice(all_entries)
    html_content = convert_markdown(random_entry)
    return render(request, "encyclopedia/entry.html",{
        "title":random_entry,
        "content":html_content
    })