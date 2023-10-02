from django.urls import path
from . import views

app_name='Recipies'

urlpatterns=[
    path('',views.index,name='index'),
    path('recipie/<int:recipie_id>/',views.detail,name='detail'),
    path('add/',views.add_recipie,name="add_recipie"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name='delete'),
    # path('review/<int:id>/',views.review,name='review'),

]