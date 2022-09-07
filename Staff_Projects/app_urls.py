from django.urls import path
from . import views

urlpatterns = [
    # Project details urls:
    path('',views.login_admin,name='login'),
    path('logout_admin/',views.logout_admin,name='logout'),
    path('home/',views.projects_page,name='home_set'),
    path('home/completed/<int:id>/',views.projects_complete,name='done'),
    path('home/adding_project/',views.adding_project,name='adding_project'),
    path('home/update_project/<int:up_id>/',views.update_project,name='update_project'),
    path('home/delete_project/<int:dl_id>/',views.delete_project,name='dl_project'),
    path('home/project_details/<int:id_num>/',views.project_details,name='proj_dtls'),
    path('home/deleteAll/',views.deleteAll, name='all_dl'),
    # Staff details urls:
    path('home/staff/',views.staff,name='staff'),
    path('home/staff/employee/<int:prf_id>/',views.personal, name='info'),
    path('home/adding_employee/',views.adding_employee,name='add_employee'),
    path('home/update_employee/<int:up_id>/',views.update_employee,name='update_employee'),
    path('home/delete_employee/<int:dl_id>/',views.delete_employee,name='dl_employee'),
]

