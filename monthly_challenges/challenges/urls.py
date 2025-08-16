from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Will trigger the index view
    path("<int:month>",views.monthly_challenge_by_number, name="month-challenge-by-number"),
    path("<str:month>", views.monthly_challenge, name="month-challenge") # e.g., /january, /february
]