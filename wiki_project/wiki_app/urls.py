from django.urls import path
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
    # edit related item
    path('edit_related/<int:item_id>/', views.edit_related, name='edit_related'),
    # delete related item
    path('delete_related/<int:item_id>', views.delete_related, name='delete_related'),
]
