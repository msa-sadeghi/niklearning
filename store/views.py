from .forms import Register
from django.shortcuts import render
from .models import Tutorial
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from urllib.parse import unquote
from .models import Tutorial
from .models import Tutorial
from decimal import Decimal
from django.http import JsonResponse


def store_home(request):
    all_tutorials = Tutorial.objects.all()
    return render(request, "store/home.html", {'tutorials': all_tutorials})


def product_details(request, slug, *args, **kwargs):
    product = get_object_or_404(Tutorial, slug=slug)
    total_price = product.total_price/10
    episode_price = product.episode_price/10
    total_price_online = product.total_price_online/10
    episode_price_online = product.episode_price_online/10
    return render(request, "store/product_details.html", {'product': product, 'total_price':total_price, 'episode_price':episode_price, 'total_price_online':total_price_online, 'episode_price_online':episode_price_online })

def calc_total_price_per_user_selection(request):
    total_price_per_user_selected_options = 0
    if request.POST:
        id = request.POST.get('tutorial_data_id')
        online_or_offline = request.POST.get('select_tutorial')
        episode_number = request.POST.get('value_episode')
        tutorial = Tutorial.objects.get(pk=id)
        episode_price = 0
        if online_or_offline == 'online':
            episode_price = tutorial.episode_price_online
        else:
            episode_price = tutorial.episode_price
        total_price_per_user_selected_options = Decimal(episode_number) * episode_price
        request.session['amount'] = float(total_price_per_user_selected_options)
        total_price_per_user_selected_options_toman = total_price_per_user_selected_options / 10
    return JsonResponse({'total_price_per_user_selected_options':total_price_per_user_selected_options, 'total_price_per_user_selected_options_toman':total_price_per_user_selected_options_toman})

def register(request, tut_name=None):
    
    submitted = False
    tutorial_data = None
    if tut_name == None:
        tutorial_data = Tutorial.objects.all().first() # for sending to register page for displaying the tutorial details in which user selected
    if tut_name != None:
        tut_name = unquote(str(tut_name)) # for display which tutorial is selected in select options
        tutorial_data = Tutorial.objects.get(name=tut_name) # for sending to register page for displaying the tutorial details in which user selected
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        submitted = True
        # create a form instance and populate it with data from the request:
        form = Register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            family = form.cleaned_data['family']
            request.session['family'] = family
            age = form.cleaned_data['age']
            request.session['age'] = age
            email = form.cleaned_data['email']
            request.session['email'] = email
            mobile = form.cleaned_data['mobile']
            request.session['mobile'] = mobile
            tutorial = form.cleaned_data['tutorial']
            request.session['tutorial'] = tutorial
            type = form.cleaned_data['type']
            request.session['type'] = tutorial
            return redirect("/zarinpal/request")

    # if a GET (or any other method) we'll create a blank form
    else:
        submitted = False
        form = Register(request.GET)
        
    # these variables are for converting rial to toman
    total_price = tutorial_data.total_price/10
    episode_price = tutorial_data.episode_price/10
    total_price_online = tutorial_data.total_price_online/10
    episode_price_online = tutorial_data.episode_price_online/10

    return render(request, 'store/register.html', {'form': form, 'name':tut_name, 'submitted':submitted, 'tutorial_data':tutorial_data, 'total_price':total_price, 'episode_price':episode_price, 'total_price_online':total_price_online, 'episode_price_online':episode_price_online})
