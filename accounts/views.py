from django.contrib.auth import logout as logout_user
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from .models import User
from .decorators import login_required, email_required

# Create your views here.
@email_required
def home(request):
    return render(request, 'main.html')

def auth_with(request):
    return render(request, 'auth_with.html')

@login_required
def editPage(request):
    profile = User.objects.get(id=request.user.id)
    form = CustomUserCreationForm(instance=profile)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return render(request, 'main.html')
    context = {'form': form}
    return render(request, 'profile_edit.html', context)

@login_required
def logout(request):
    logout_user(request)
    return redirect('/')

@email_required
def profile(request, pk):
    profile_page = User.objects.get(id = pk)
    context = {'user':profile_page}
    return render(request, 'profile.html', context)

@login_required
def profiles_list(request):
    profiles = User.objects.all()
    context = {'users':profiles}
    return render(request, 'profiles_list.html', context)

