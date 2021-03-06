from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def login_view(request) :
    if request.method == "POST" :
        form = AuthenticationForm(request=request, data= request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)

            if user is not None :
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, "account.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST" :
        #우리가 폼으로 받은 데이터로 유저를 만들어야하기 때문
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            #회원가입 하자마자 로그인 된 상태
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
        return render(request, "account.html", {"form":form})
