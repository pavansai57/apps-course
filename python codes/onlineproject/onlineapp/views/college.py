from django.urls import reverse_lazy
from django.views import View
from onlineapp.models import College
from django.shortcuts import get_object_or_404, redirect

from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import render_to_response

import onlineapp.models
from onlineapp.models import *
import ipdb

from onlineapp.views.forms1 import *


class CollegeView(View):

    def get(self,request,*args,**kwargs):
        colleges = College.objects.values()
        ipdb.set_trace()


        return render(request,template_name="templates/collegelist.html",context={'college':colleges})

        pass


from django.views.generic import *




class CollegeListView(ListView):
    model=College
    context_object_name='college'
    template_name = 'templates/collegelist.html'



    def get_context_data(self,**kwargs):
        context=super(CollegeListView,self).get_context_data(**kwargs)
        #ipdb.set_trace()

        return context


    pass


class CollegeDetailView(DetailView):

    model=College
    template_name="templates/student_detail.html"

    def get_object(self):
        return get_object_or_404(College,**self.kwargs)

    def get_context_data(self,**kwargs):
        #ipdb.set_trace()
        context=super(CollegeDetailView,self).get_context_data(**kwargs)
        college=context.get("college")
        students=list(college.student_set.values("name","email","mocktest1__total").order_by("-mocktest1__total"))
        context.update({'student':students,"college_id":college.id})
        return context


class CollegeDetailView2(DetailView):

    model=College
    template_name="templates/student_detail.html"

    def get_object(self):
        return get_object_or_404(College,**self.kwargs)

    def get_context_data(self,**kwargs):
        #ipdb.set_trace()
        context=super(CollegeDetailView2,self).get_context_data(**kwargs)
        college=context.get("college")
        students=list(college.student_set.values("name","email","mocktest1__total").order_by("-mocktest1__total"))
        context.update({'student':students})
        return context

class AddCollege(CreateView):
    form_class=CollegeForm
    template_name='templates/addcollege.html'
    success_url=reverse_lazy("onlineapp:colleges_html")

""""def get(self,request,*args,**kwargs):
        ipdb.set_trace()
        form1 = CollegeForm()
        return render(request,template_name="templates/addcollege.html",context={'form':form1})"""

class AddStudent(CreateView):
    form_class=StudentForm
    model=Student
    template_name = "templates/addstudent.html"
    success_url = reverse_lazy("onlineapp:colleges_html")

    def get_context_data(self, **kwargs):
        context=super(AddStudent,self).get_context_data(**kwargs)
        mock_form=MockForm
        student_mock=StudentForm
        context.update({
            'student_form': context.get('form'),
            'mock_form': mock_form
        })

        return context

    def post(self, request, *args, **kwargs):
        college=get_object_or_404(College,pk=self.kwargs.get("college_id"))
        student_form=StudentForm(request.POST)
        mock_form=MockForm(request.POST)
        ipdb.set_trace()
        if student_form.is_valid():
            student=student_form.save(commit=False)
            student.college=college
            student.save()

            if mock_form.is_valid():
                mocktest=mock_form.save(commit=False)
                ipdb.set_trace()
                mocktest.total=mocktest.problem1+mocktest.problem2+mocktest.problem3+mocktest.problem4
                mocktest.student=student
                mocktest.save()
        return redirect("onlineapp:colleges_html")
        pass

"""    def post(selfself,request,*args,**kwargs):
        college=get_object_or_404(College,)
"""

class UpdateCollegeView(UpdateView):
    model=College
    template_name="templates/addcollege.html"
    form_class=CollegeForm
    success_url = reverse_lazy('onlineapp:colleges_html')
"""    def get_object(self,queryset=None):
        cd=get_object_or_404(College,pk=self.kwargs.get('id'))
        ipdb.set_trace()
        return get_object_or_404(College,pk=self.kwargs.get('id'))
"""

class DeleteCollegeView(DeleteView):
    model=College
    form_class=CollegeForm
    template_name="templates/college_confirm_delete.html"
    #success_url =reverse_lazy("onlineapp:colleges_html")  ## redirect giving circular import

    def post(self,request,*args,**kwargs):
        if kwargs:
            get_object_or_404(College,**kwargs).delete()
            return redirect("onlineapp:colleges_html")

"""    def get_object(self,queryset=None):
        get_object_or_404(College, pk=self.kwargs.get('id'))
    success_url = reverse_lazy("onlineapp:colleges_html")
"""
"""    def post(self,request,*args,**kwargs):
        if kwargs:
            get_object_or_404(College,**kwargs).delete()
            redirect("onlineapp:colleges_html")
            retur
"""