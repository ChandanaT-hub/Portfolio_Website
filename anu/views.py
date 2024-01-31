from django.shortcuts import render
from.models import Home,About
# Create your views here.
def index(request):
    #home
    home = Home.objects.latest('updated')

    # about
    about = About.objects.latest('updated')
    #profiles=Profile.objects.filter(about=about)
    #skills=Skills.objects.latest('updated')
    #categories = Category.objects.all()
    context = {
        'home': home,
        'about':about,

        #'profiles':profiles,
        #'categories':categories,

    }

    return render(request,'index.html', context)