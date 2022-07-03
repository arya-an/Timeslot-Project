from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView,DeleteView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse



# Create your views here.


def all_details(request):
    candidate = RegisterModel.objects.filter(category='Candidate')
    interviewer = RegisterModel.objects.filter(category='Interviewer')
    context = {'candidate':candidate,'interviewer':interviewer}
    if request.method=='GET':
        data = request.GET
        candidateid = data.get('candidateid') 
        interviewerid = data.get('interviewerid')
        candidate_timefrom = RegisterModel.objects.filter(id=candidateid).values('avail_from')
        candidate_timeto = RegisterModel.objects.filter(id=candidateid).values('avail_to')
        interviewer_timefrom = RegisterModel.objects.filter(id=interviewerid).values('avail_from')
        interviewer_timeto = RegisterModel.objects.filter(id=interviewerid).values('avail_to')
        a=0
        for i in candidate_timefrom:
            a=(i['avail_from'])
        candtime1 = int(a)
        b=0
        for i in candidate_timeto:
            b=(i['avail_to'])
        candtime2 = int(b)
        c=0
        for i in interviewer_timefrom:
            c=(i['avail_from'])
        intertime1 = int(c)
        d=0
        for i in interviewer_timeto:
            d=(i['avail_to'])
        intertime2 = int(d)
        interviewer_timediff = intertime2-intertime1
        candidate_timediff = candtime2-candtime1

        interviewertimelist=[]
        for i in range(1,interviewer_timediff+1):
            timelist1=(intertime1,intertime1+1)
            intertime1=intertime1+1
            interviewertimelist.append(timelist1)
        

        candidatetimelist=[]
        for i in range(1,candidate_timediff+1):
            timelist2=(candtime1,candtime1+1)
            candtime1=candtime1+1
            candidatetimelist.append(timelist2)

        
        available_timeslots=[]
        for i in interviewertimelist:
            if i in candidatetimelist: 
                available_timeslots.append(i)
        
        if len(available_timeslots)!=0:
            response={'available_timeslots':available_timeslots}
            return JsonResponse(response)
            
        else:
            
            return render(request,'All_Details.html',context)
        
    return render(request,'All_Details.html',context)

class RegisterCreate(CreateView):
    model = RegisterModel
    fields = '__all__'
    template_name = 'Register.html'
    success_url = reverse_lazy('register')



