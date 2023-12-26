from django.urls import path

from jobseeker import views

urlpatterns = [

    path("register/",views.SignUpView.as_view(),name='signup'),
    path("index",views.StudentIndexView.as_view(),name='seeker-index'),
    path("profile/add",views.ProfileCreateView.as_view(),name="profile-add"),
    path("profile/<int:pk>",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profile/<int:pk>/change",views.profileEditView.as_view(),name="profile-edit"),
    path("jobs/<int:pk>",views.JobDetailView.as_view(),name='job-detail'),
    path("job/<int:pk>/apply",views.ApplyJob.as_view(),name='job-apply'),
    path("application/all",views.ApplicationsListView.as_view(),name='myapplication'),
    path("jobs/<int:pk>/save",views.JobSaveView.as_view(),name='job-save'),
    path("jobs/saved/all",views.SaveJobView.as_view(),name='saved-job')

]