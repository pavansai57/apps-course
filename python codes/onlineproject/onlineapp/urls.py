from . import views
from django.urls import path
from  onlineapp.views import *

app_name='onlineapp'


urlpatterns=[

    #path("colleges2/",CollegeView.as_view(), name="colleges_html"),
    path("colleges/",CollegeListView.as_view(),name="colleges_html"),
    path("college_detailview/<int:pk>",CollegeDetailView.as_view(),name="student_detailview"),
    path("college_detailview/<str:acronym>/",CollegeDetailView.as_view(),name="student_detailview2"),
    path("addcollege/",AddCollege.as_view(),name="add_college"),
    path("addstudent/",AddStudent.as_view(),name="add_student"),
    path("college_detailview/<int:college_id>/add",AddStudent.as_view(),name="add_student2"),
    path("colleges/<int:pk>/edit",UpdateCollegeView.as_view(),name="update_college"),
    path("colleges/<int:pk>/delete",DeleteCollegeView.as_view(),name="delete_college")
]

"""
    path('helloworld/', views.helloview),
    path('aview/', views.aview),
    path('collegeview/', views.college_name_acronym),
    path('college/', views.college),
    path('abrender/', views.abrender),
    path('college_template/', views.college_render_template),
    path('student_details/', views.student_details),
    path('student_get/', views.student_get),
    path('student/<int:id>', views.student_get2),
    path('student_marks/', views.student_marks),
    path('college_list/<slug:acronym>', views.college_list),
    path('testsession/', views.session_view),
    path('view_exception/', views.raising_exception_in_view_code),
    path('view_exception2s/', views.raising_exception_in_view_code2)
    """