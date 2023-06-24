from django.urls import path, include
from djangoProject4.notes_app_profile import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('profile/', views.check_profile, name='profile'),
    path('profile/delete', views.delete_profile, name='delete-profile'),
    path('add/', views.add_note, name='add-note'),
    path('edit/<int:pk>', views.edit_note, name='edit-note'),
    path('delete/<int:pk>', views.delete_note, name='delete-note'),
    path('details/<int:pk>', views.details_note, name='details-note'),
]
