from django.shortcuts import redirect

def home_view(request):
    """Redirect based on authentication"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
