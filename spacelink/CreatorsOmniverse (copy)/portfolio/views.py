from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Project
from .forms import PortfolioForm, ProjectForm


@login_required
def edit_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(
        user=request.user,
        defaults={
            'name': request.user.username,
            'email': request.user.email
        }
    )

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('view_portfolio', username=request.user.username)
    else:
        form = PortfolioForm(instance=portfolio)

    return render(request, 'portfolio/edit_portfolio.html', {
        'form': form,
        'portfolio': portfolio
    })


@login_required
def add_project(request):
    portfolio = get_object_or_404(Portfolio, user=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()
            return redirect('edit_portfolio')
    else:
        form = ProjectForm()

    return render(request, 'portfolio/add_project.html', {'form': form})


def view_portfolio(request, username):
    portfolio = get_object_or_404(Portfolio, user__username=username)

    if not portfolio.is_public and request.user != portfolio.user:
        return render(request, 'portfolio/private.html')

    template_name = f'portfolio/themes/{portfolio.theme}.html'
    return render(request, template_name, {'portfolio': portfolio})
