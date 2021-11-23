from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index-function'),
    path('form/', views.FORM, name='form-function'),
    path('list/', views.View_List, name='list-function'),
    path('delete/<delete_id>', views.delete, name='delete'),
    path('update/<update_id>', views.update, name='update'),

]