from django.shortcuts import render


# home page
def index(request):
    return render(request, 'wiki_app/index.html')


# view entry
def view_entry(request, post_id):
    return render(request, 'wiki_app/view_entry.html')


# create ne user
def new_user(request):
    return render(request, 'wiki_app/new_user.html')


# view user entries
def my_entries(request):
    return render(request, 'wiki_app/my_entries.html')


# add new entry
def new_entry(request):
    return render(request, 'wiki_app/new_entry.html')


# edit entry
def edit_entry(request):
    return render(request, 'wiki_app/new_entry.html')


# delete entry
def delete_entry(request):
    return render(request, 'wiki_app/delete_entry.html')


# add new related item
def new_related(request):
    return render(request, 'wiki_app/new_related.html')


# edit related item
def edit_related(request):
    return render(request, 'wiki_app/new_related.html')


# delete related item
def delete_related(request):
    return render(request, 'wiki_app/delete_related.html')
