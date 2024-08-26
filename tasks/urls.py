from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks completed'),
    path('tasks/<int:task_id>', views.task_detail, name='task detail'),
    path('tasks/<int:task_id>/complete', views.task_complete, name='task complete'),
    path('tasks/<int:task_id>/delete', views.task_delete, name='task delete'),
    path('task/create', views.create_task, name='create task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]