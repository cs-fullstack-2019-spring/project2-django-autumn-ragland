from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    # home page view and search all entries
    path('', views.index, name='index'),
    # view entry
    path('view_entry/<int:entry_id>/', views.view_entry, name='view_entry'),
    # new user
    path('new_user/', views.new_user, name='new_user'),

    # view and edit user entries
    path('my_entries/', views.my_entries, name='my_entries'),

    # add entry
    path('new_entry/', views.new_entry, name='new_entry'),
    # edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # delete entry
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),

    # add related item
    path('new_related/<int:entry_id>/', views.new_related, name='new_related'),
    # view related items to edit
    path('view_related/<int:entry_id>', views.view_related, name='view_related'),
    # edit related item
    path('edit_related/<int:item_id>/', views.edit_related, name='edit_related'),
    # delete related item
    path('delete_related/<int:item_id>', views.delete_related, name='delete_related'),

    # image field render
    path('images/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),

    # search bar
    path('search/', views.search, name='search'),
]
