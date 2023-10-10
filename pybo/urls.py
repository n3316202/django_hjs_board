from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'), #http://localhost:8000/pybo/<int:question_id>/  -> http://localhost:8000/pybo/2/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
