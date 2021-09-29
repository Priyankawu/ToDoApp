from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addToDo, name='add'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
    path('deleteComplete', views.deleteComplete, name='deleteComplete'),
    path('complete/<todo_id>', views.completeTodo, name = 'complete')
    
]