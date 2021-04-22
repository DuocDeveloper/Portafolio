from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subcripcion import views

urlpatterns = [
    path('subcripciones', views.SubcripcionList.as_view()),
    path('subcripciones/<int:pk>', views.SubcripcionDetail.as_view())
]
