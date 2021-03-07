from django.shortcuts import redirect, render

def login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('accounts:auth_with')
    return wrapper_func

def email_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if len(request.user.email) > 0:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('accounts:profile_edit')
        else:
            return redirect('accounts:auth_with')
    return wrapper_func