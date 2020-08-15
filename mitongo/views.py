from django.shortcuts import render,  redirect, get_object_or_404
#from .forms import RestaurantLocationsForm
from django.http import HttpResponse
from .models import RestaurantLocation
from .forms import  CreateUserForm, RestaurantLocationForm
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
# its a flash messages
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,

)

class RestaurantListView(ListView):
    model = RestaurantLocation
    template_name = 'take.html'


class RestaurantDetail(DetailView):
    model = RestaurantLocation
    template_name = 'detail.html'




class RestaurantUpdate(UpdateView):
    model = RestaurantLocation
    template_name = 'update.html'
    fields = ['Username', 'Password', 'PasswordConfirmation']
    success_url = reverse_lazy ('Restaurant_take')



class RestaurantDelete(DeleteView):
    model = RestaurantLocation
    template_name = 'delete.html'


class RestaurantCreate(CreateView):
    model = RestaurantLocation
    template_name = 'create.html'
    fields = '__all__'


# the default conform django give us 
def registerPage(request):
    form =  CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect ('loginPage')

    context ={'form':form}
    template_name= 'user.html'
    return render(request, template_name, context)

# DJANGO BUILD IN FORM 
def loginPage(request):

    if request.method =='POST':
        username = request.POST.get('username') # its grabe username  in the login template and authenticate it 
        password = request.POST.get('password')# this password get it in template plz mind case sensitive
        user = authenticate(request, username=username, password=password) #here we authenticate username and password
        #print(user)
        if user is not None:
            login(request, user) # this login its from above
            return redirect('/') # the name in the urls
    #context ={'form':form}
    template_name= 'login.html'
    return render(request, template_name) #, context)











def Restaurant_Create(request):
    form    = RestaurantLocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form    = RestaurantLocationsForm()
    template_name = 'mito_create.html'
    context = { 'form': form}
    return render (request, template_name, context)


def Restaurant(request):
    
    template_name = 'draft.html'
    context = { 'object': 'RUTH RESTAURANT'}
    return render (request, template_name, context)

def Restaurant_Update(request, pk=None):
    queryset     = get_object_or_404(RestaurantLocation, id=pk)
    form    = RestaurantLocationForm(request.POST or None, instance= queryset )
    if form.is_valid():
        form.save()
        form    = RestaurantLocationForm()
      
    template_name = 'update.html'
    context = { 'form': form}
    return render (request, template_name, context)


def mpoyi_retreive(request, pk=None):

    queryset            = RestaurantLocation.objects.get(id=pk)
    templates_name      = 'retreive.html'
    context             = {'object':queryset }
    return render(request, templates_name, context)



def exercise_frontend(request):
    template_name = "exercise.html"
    return render (request, template_name)