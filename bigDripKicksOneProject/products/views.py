from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import LatestArrival 
from .models import TopSeller
from .models import Drip 
from .models import Kicks
# from django.http import StreamingHttpResponse
# Create your views here.


def home(request, *args, **kwargs):
    # return HttpResponse("<h1>Live Soccer Matches</h1>")
    # get all live soccer matches
    # obj =  SoccerMatch.objects.all()
    return render(request, "home.html", {})

def drip(request):
    # obj =  FootballMatch.objects.all()
    return render(request, "drip.html")

def kicks(request):
    #  obj =  FightMatch.objects.all()
     return render(request, "kicks.html")

def aboutus(request):
    # obj =  BasketballMatch.objects.all()
    return render(request, "aboutus.html")

