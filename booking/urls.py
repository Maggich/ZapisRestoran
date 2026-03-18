from django.urls import path
from . import views
urlpatterns = [
    path('', views.hall, name="hall"),
    path('reserve/<int:table_id>/', views.reserve, name="reserve")
]
