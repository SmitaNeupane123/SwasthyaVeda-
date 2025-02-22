from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from .serializers import RegisterSerializer

User = get_user_model()

def register_view(request):
    if request.user.is_authenticated:
        if request.user.role == 'doctor':
            return redirect('doctor_dashboard', doctor_id=request.user.id)
        elif request.user.role == 'nurse':
            return redirect('nurse_dashboard', nurse_id=request.user.id)
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            return redirect('login')  
        else:
            return render(request, 'signup.html', {'errors': serializer.errors})
    return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        if request.user.role == 'doctor':
            return redirect('doctor_dashboard', doctor_id=request.user.id)
        elif request.user.role == 'nurse':
            return redirect('nurse_dashboard', nurse_id=request.user.id)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'doctor':
                return redirect('doctor_dashboard', doctor_id=user.id)
            elif user.role == 'nurse':
                return redirect('nurse_dashboard', nurse_id=user.id)
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request) 
    return redirect('home')  

def doctor_dashboard(request, doctor_id):
    if not request.user.is_authenticated:
        return redirect('login') 

    doctor = get_object_or_404(User, id=doctor_id, role='doctor')
    if request.user != doctor:
        return redirect('home')  
    return render(request, 'doctor_dashboard.html', {'doctor': doctor})


def nurse_dashboard(request, nurse_id):
    if not request.user.is_authenticated:
        return redirect('login')  

    nurse = get_object_or_404(User, id=nurse_id, role='nurse')
    if request.user != nurse:
        return redirect('home')  

    return render(request, 'nurse_dashboard.html', {'nurse': nurse})

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'doctor':
            return redirect('doctor_dashboard', doctor_id=request.user.id)
        elif request.user.role == 'nurse':
            return redirect('nurse_dashboard', nurse_id=request.user.id)
    return render(request, 'index.html')
