from django.shortcuts import render,redirect  
from django.contrib.auth import authenticate, login
#from django.contrib.auth.forms import UserCreationFormib
from django.contrib.auth.models import User
from .models import Regist
from .forms import NewRegist, LoginForm, NewTarea
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

def home(request):
    if request.method == 'GET':
       form = LoginForm()
       return render(request, 'app/home.html')
    else:
        password = request.POST.get('password')
        hashed_password = make_password(password)
        datosM = request.POST.copy() 
        datosM['password']=hashed_password
        form = LoginForm(datosM)
       
        print(form)
        if form.is_valid():
            
            nombre_usuario = form.cleaned_data['email']
            contraseña = form.cleaned_data['password']
            user = authenticate(request, username=nombre_usuario, password=contraseña)
            if user is not None:
                login(request, user)
                print(request , ' ESTO ES DEL USER')
                return redirect('app/prueva.html')  # Redirige a la página de inicio del usuario
        else:
            form = LoginForm()
            return HttpResponse('esta mal')
            #return render(request, 'app/home.html')
    # print(request.POST)
    # return render(request, 'app/home.html')


def comida(request):
    if request.method == 'GET':
        return render(request, 'app/comida.html')
    else:
        password = request.POST.get('password')
        # Encriptar la contraseña
        hashed_password = make_password(password)
        datosM = request.POST.copy() 
        datosM['password']=hashed_password
        form= NewRegist(datosM)
        if request.POST['password'] == request.POST['password2']:
            #form = NewRegist(request.POST).
           print(datosM)
           if form.is_valid():
            form.save()
            # formulario=form.save()
            # formulario.set_password(form.cleaned_data['password'])
            print(request.POST.get('nombre'))
           else:
               #eturn HttpResponse('El')
               form = NewRegist()
               return render(request, 'app/comida.html',{'form': form})
        else:
            return HttpResponse('La contraseña esta mal')
    return redirect('/')     
   
   

def principal(request):
    
    return render(request, 'app/principal.html')

def prueva(request):
    if request.method == "GET":
        print('Todo bien')
    else:
        
        form= NewTarea(request.POST)
        print(form)
        if form.is_valid():
             form.save()
        else:
            form = LoginForm()
            return HttpResponse('esta mal')
    return render(request, 'app/prueva.html')
def ajustes(request):
    return render(request, 'app/ajustes.html')

def post(request):
    print(request.POST)
    return redirect('home')


