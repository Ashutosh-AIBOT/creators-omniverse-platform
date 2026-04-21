from django.shortcuts import render

def chatbot_page(request):
    # This just renders the HTML file located in your templates folder
    return render(request, 'xomni/index.html')