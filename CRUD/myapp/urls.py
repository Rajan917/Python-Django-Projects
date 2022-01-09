from django.urls import path
from . import views
urlpatterns = [
    path('',views.studentdata, name='addstudent'),
    path('delete/<int:id>',views.delete_data, name='deletedata'),
    path('<int:id>/',views.edit_data,name='editdata')
]