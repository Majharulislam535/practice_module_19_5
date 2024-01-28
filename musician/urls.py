from django.urls import path,include
from .import views

urlpatterns = [
    path('add_musician/',views.Create_Musician.as_view(),name='add_musician'),
    path('edit_musician/<int:id>',views.Edit_Musician.as_view(),name='edit_musician'),
    path('delete_musician/<int:id>',views.Delete_Musician.as_view(),name='delete_musician'),
]