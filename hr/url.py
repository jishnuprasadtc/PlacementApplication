from django. urls import path
from hr import views



urlpatterns=[
    path("",views.SignInView.as_view(),name="signin"),
    path("dashboard",views.DashBoardView.as_view(),name='index'),
    path("logout",views.SignOutView.as_view(),name='remove'),
    path("category",views.CategoryListCreateView.as_view(),name="category"),
    path("category/<int:pk>/remove",views.categoryDeleteView.as_view(),name="remove"),
    path("job/add",views.CreateJobView.as_view(),name="jobadd"),
    path("job/all",views.JobListView.as_view(),name="job-list"),
    path("job/<int:pk>/delete",views.JobDeleteView.as_view(),name='job-delete'),
    path("job/<int:pk>/change",views.JobUpdateView.as_view(),name="job-edit")
    
]


