from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserModel, EnrtyModel, EntryForm, RelatedItemForm, RelatedItemModel
from django.contrib.auth.models import User


# view all wiki entries
def index(request):
    all_entries = EnrtyModel.objects.all()
    context = {
        'all_entries': all_entries
    }
    return render(request, 'wiki_app/index.html', context)


# view a wiki on click entry
def view_entry(request, entry_id):
    entry = EnrtyModel.objects.get(pk=entry_id)
    context = {
        'entry': entry
    }
    return render(request, 'wiki_app/view_entry.html', context)


# create new user
def new_user(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST':
        User.objects.create_user(request.POST['name'], "", request.POST['password'])
        form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'wiki_app/new_user.html', context)


# view user entries
def my_entries(request):
    if request.user.is_authenticated:
        current_user = UserModel.objects.get(name=request.user)
        user_entries = EnrtyModel.objects.filter(user_model_fk=current_user)
        context = {
            'my_entries': user_entries
        }
    else:
        user_entries = ''
        context = {
            'user_entries': user_entries
        }

    return render(request, 'wiki_app/my_entries.html', context)


# add new entry
def new_entry(request):
    if request.user.is_authenticated:
        form = EntryForm(request.POST or None)
        current_user = UserModel.objects.get(name=request.user)
        if request.method == 'POST':
            EnrtyModel.objects.create(title=request.POST['title'], text=request.POST['text'], image=request.POST['image'],
                                      user_model_fk=current_user)
            # form.save()
            return redirect('index')

        context = {
            'form': form
        }
    else:
        form = ''
        context = {
            'form': form
        }

    return render(request, 'wiki_app/new_entry.html', context)


# edit entry
def edit_entry(request, entry_id):
    entry_item = get_object_or_404(EnrtyModel, pk=entry_id)
    form = EntryForm(request.POST or None, instance=entry_item)
    if request.method == 'POST':
        form.save()
        return redirect('my_entries')
    context = {
        'form': form
    }
    return render(request, 'wiki_app/new_entry.html', context)


# delete entry
def delete_entry(request, entry_id):
    entry_item = get_object_or_404(EnrtyModel, pk=entry_id)
    if request.method == 'POST':
        entry_item.delete()
        return redirect('my_entries')
    context = {
        'item': entry_item
    }
    return render(request, 'wiki_app/delete_entry.html', context)


# add new related item
def new_related(request, entry_id):
    return render(request, 'wiki_app/new_related.html')


# edit related item
def edit_related(request, item_id):
    return render(request, 'wiki_app/new_related.html')


# delete related item
def delete_related(request, item_id):
    return render(request, 'wiki_app/delete_related.html')
