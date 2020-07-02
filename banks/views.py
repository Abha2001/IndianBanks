from django.shortcuts import render,redirect
from .models import Banks,Branches
from .serializers import BranchesSerializer, BanksSerializer
from rest_framework import viewsets, generics
from .forms import SearchDataForm, SearchIFSCForm
# Create your views here.

class BanksViewSet(viewsets.ModelViewSet):
    queryset= Banks.objects.all()
    serializer_class= BanksSerializer

class BranchesViewSet(viewsets.ModelViewSet):
    queryset= Branches.objects.all()
    serializer_class= BranchesSerializer

class SearchBranchesList(generics.ListAPIView):
    serializer_class= BranchesSerializer

    def get_queryset(self):
        if(self.request.query_params.get('Bank')):
            name= self.request.query_params.get('Bank')
            city= self.request.query_params.get('City')
            return Branches.objects.filter(bank__name__iexact=name, city__iexact=city)
        elif (self.request.query_params.get('IFSCCode')):
            ifsc= self.request.query_params.get('IFSCCode')
            return Branches.objects.filter(ifsc=ifsc)
        else:
            return Branches.objects.none()


def index(request):
    context={}
    form1= SearchDataForm()
    form2= SearchIFSCForm()
    context['form1']=form1
    context['form2']=form2
    return render (request, 'banks/search.html',context)