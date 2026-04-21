from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request, username=None):
    if request.user.is_authenticated:
        # If username not in URL or doesn't match logged in user, redirect to correct URL
        if username != request.user.username:
            return redirect('universe:home', username=request.user.username)
        # User is logged in and URL username matches
        context = {
            'username': request.user.username
        }
        return render(request, "universe/home.html", context)
    else:
        # User not logged in, show public home page
        return render(request, "universe/phome.html")
