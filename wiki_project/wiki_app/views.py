from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserModel, EnrtyModel, EntryForm, RelatedItemForm, RelatedItemModel
from django.contrib.auth.models import User


# view all wiki entries
def index(request):
    # get all entries
    all_entries = EnrtyModel.objects.all()
    # pass entries
    context = {
        'all_entries': all_entries
    }
    # render home page
    return render(request, 'wiki_app/index.html', context)


# view a wiki on click entry
def view_entry(request, entry_id):
    # get entry
    entry = EnrtyModel.objects.get(pk=entry_id)
    # get related info
    related_info = RelatedItemModel.objects.filter(entry_model_fk=entry)
    # pass entry and related info
    context = {
        'entry': entry,
        'related': related_info
    }
    print(entry.image.path)
    print(entry.image.url)
    print(entry.image.name)
    # render view entry
    return render(request, 'wiki_app/view_entry.html', context)


# create new user
def new_user(request):
    # grab empty user form
    form = UserForm(request.POST or None)

    if request.method == 'POST':
        # on submit add users to model and django table
        User.objects.create_user(request.POST['name'], "", request.POST['password'])
        form.save()
        # on submit render home page
        return redirect('index')
    # pass empty user form
    context = {
        'form': form
    }
    # render user form page
    return render(request, 'wiki_app/new_user.html', context)


# view user entries
def my_entries(request):
    # only for logged in users
    if request.user.is_authenticated:
        # determine logged in user and model fk filter
        current_user = UserModel.objects.get(name=request.user)
        user_entries = EnrtyModel.objects.filter(user_model_fk=current_user)
        # pass filtered entries
        context = {
            'my_entries': user_entries
        }
    # for users not logged in
    else:
        user_entries = ''
        context = {
            'user_entries': user_entries
        }
    # render user entry page
    return render(request, 'wiki_app/my_entries.html', context)


# add new entry
def new_entry(request):
    # for logged in users
    if request.user.is_authenticated:
        # get empty entry form
        form = EntryForm(request.POST or None)
        # determine logged in user
        current_user = UserModel.objects.get(name=request.user)
        if request.method == 'POST':
            # on submit add entry to model with logged in user fk
            EnrtyModel.objects.create(title=request.POST['title'], text=request.POST['text'],
                                      update_date=request.POST['update_date'], image=request.FILES['image'],
                                      user_model_fk=current_user)
            # on submit render home page
            return redirect('index')
        # pass empty user form
        context = {
            'form': form
        }
    # for users not logged in
    else:
        form = ''
        context = {
            'form': form
        }
    # render new entry form page
    return render(request, 'wiki_app/new_entry.html', context)


# edit entry
def edit_entry(request, entry_id):
    # grab entry to edit
    entry_item = get_object_or_404(EnrtyModel, pk=entry_id)
    # populate entry form
    form = EntryForm(request.POST or None, instance=entry_item)

    if request.method == 'POST':
        # on submit save edits
        form.save()
        # on submit redirect to my entries page
        return redirect('my_entries')
    # pass populated entry form
    context = {
        'form': form
    }
    # render new entry page with POPULATED form
    return render(request, 'wiki_app/new_entry.html', context)


# delete entry
def delete_entry(request, entry_id):
    # grab specific entry
    entry_item = get_object_or_404(EnrtyModel, pk=entry_id)

    if request.method == 'POST':
        # on submit delete entry
        entry_item.delete()
        # on submit render my entries page
        return redirect('my_entries')
    # pass specific entry
    context = {
        'item': entry_item
    }
    # render confirmation form
    return render(request, 'wiki_app/delete_entry.html', context)


# add new related item
def new_related(request, entry_id):
    # grab empty related item form
    form = RelatedItemForm(request.POST or None)
    # grab entry fk
    linked_entry = get_object_or_404(EnrtyModel, pk=entry_id)

    if request.method == 'POST':
        # on submit add related item to model with entry fk
        RelatedItemModel.objects.create(title=request.POST['title'], text=request.POST['text'],

                                        image=request.FILES['image'], entry_model_fk=linked_entry)
        return redirect('index')
    # pass empty related item form
    context = {
        'form': form
    }
    # render blank related item form
    return render(request, 'wiki_app/new_related.html', context)


# edit related item BROKEN
def edit_related(request, item_id):
    related_item = get_object_or_404(RelatedItemModel, pk=item_id)
    form = RelatedItemForm(request.POST or None, instance=related_item)
    if request.method == 'POST':
        form.save()
        return redirect('my_entries')
    context = {
        'form': form
    }
    return render(request, 'wiki_app/new_related.html', context)


# delete related item BROKEN
def delete_related(request, item_id):
    related_item = get_object_or_404(RelatedItemModel, pk=item_id)
    if request.method == 'POST':
        related_item.delete()
        return redirect('my_entries')
    context = {
        'item': related_item
    }
    return render(request, 'wiki_app/delete_related.html', context)
