from django.urls import path
from .import views

urlpatterns = [
    path('add_album/', views.Create_Album.as_view(),name='Add_album'),
    path('edit_album/<int:id>', views.Edit_Album.as_view(),name='edit_album'),
]
