from django.urls import path
from Autorization.views import puzzle_function, puzzle_dunction

urlpatterns = [
    path("auth/puzzle_f", puzzle_function),
    path("auth/puzzle_d", puzzle_dunction)
]







