from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView



from jobseeker.forms import Registration,ProfileForm
from myapp.models import StudentProfile,Jobs,Applications

# Create your views here.

class SignUpView(CreateView):
    template_name="jobseeker/registrion.html"
    form_class=Registration
    success_url=reverse_lazy("signin")


class StudentIndexView(ListView):
    template_name="jobseeker/index.html"
    context_object_name="data"
    model=Jobs


    def get_queryset(self):
        my_application=Applications.objects.filter(student=self.request.user).values_list("job",flat=True)
        qs=Jobs.objects.exclude(id__in=my_application).order_by("-Create_date")
        return qs
    




class ProfileCreateView(CreateView):
    template_name="jobseeker/profile_add.html"
    form_class=ProfileForm
    success_url=reverse_lazy("seeker-index")

    def form_valid(self, form):
        form.instance.user=self.request.user
    
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    template_name="jobseeker/profile_detail.html"
    context_object_name="data"
    model=StudentProfile


class profileEditView(UpdateView):
    template_name="jobseeker/Profile_edit.html"
    form_class=ProfileForm
    model=StudentProfile
    success_url=reverse_lazy("seeker-index")


class JobDetailView(DetailView):
    template_name="jobseeker/job_detail.html"
    model=Jobs
    context_object_name="data"


class ApplyJob(View):
    def post(self,request,*args,**kwargs): 
        id=kwargs.get("pk")
        job_object=Jobs.objects.get(id=id)
        student_object=request.user
        Applications.objects.create(job=job_object,student=student_object)
        return redirect('seeker-index')



class ApplicationsListView(ListView):
    template_name="jobseeker/application.html"
    model=Applications
    context_object_name="data"


    def get_queryset(self):
        qs=Applications.objects.filter(student=self.request.user)
        return qs


# class JobListview(ListView):
#     template_name="jobseeker/Job_list.html"
#     context_object_name="jobs"
#     model=Jobs
    