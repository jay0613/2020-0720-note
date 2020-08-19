from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/note/add
    path('add',views.add_view),
    # 127.0.0.1:8000/note/show
    path('show', views.show_content),
    path('delete', views.delete),

]
