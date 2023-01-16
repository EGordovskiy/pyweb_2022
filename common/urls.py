from django.urls import path

from .views import CurrentDateView, HelloWorld, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('hello/', HelloWorld.as_view()),
]
