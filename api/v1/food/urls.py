from django.urls import path
from api.v1.food.views import foods, singleFood, create, delete, update

urlpatterns = [
    path("",foods),
    path("view/<int:pk>/",singleFood),
    path("create/",create),
    path('delete/<int:pk>/',delete),
     path('update/<int:pk>/',update),
] 
