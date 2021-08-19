from django.shortcuts import render,redirect


def authenticated_user(view_func):
    def container(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
            
        else:
            return redirect('/')
            
    return container

def allowed_users(allowed_role=[]):
    def decorator(view_func):
        def container(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_role:
                return view_func(request,*args,**kwargs)
            else:
                return redirect('home')
        return container
    return decorator
        