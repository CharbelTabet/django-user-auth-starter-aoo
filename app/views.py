from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, "home.html", {"object_list": User.objects.all()})

class signin(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(signin, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username = self.request.POST['username'],
            password = self.request.POST['password'],
                )
        if user is not None:
            login(self.request, user)
            redirect('/')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class register(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class signout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class users(ListView):
    template_name = "users.html"
    model = User

class results(View):
    template_name = "results.html"

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search_query')
        if len(search_query):
            try:
                search_results = User.objects.get(username=search_query)
            except:
                exists = False
            else:
                exists = True
            context = {
                'search_query': search_query,
                'exists': exists
            }
            return render(request, self.template_name, context)
            
        else:
            return redirect('/')
