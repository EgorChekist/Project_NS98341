from todo_list.views import todo_big_list, check_url_deleting, stick_stuff, puzzle_function
from django.urls import path

urlpatterns = [
    path("", todo_big_list),
    path("todo/<int:pk>/delete", check_url_deleting),
    path("todo/<int:pn>/update", stick_stuff),
    path("todo/puzzle", puzzle_function)
]