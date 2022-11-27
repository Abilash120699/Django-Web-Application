from django.urls import path
from expense import views
urlpatterns = [
    path('', views.example, name="expenses"),
    path('add-expense', views.example_2, name="expenses_2")

]