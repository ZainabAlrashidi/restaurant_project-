from django.shortcuts import render

# Create your views here.
def index(request):
    # this view returns the main page of the programming platform
    return render(request, 'restaurantModule/index.html')