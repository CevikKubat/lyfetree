
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index_view(request):
    # Add any context data you want to pass to the template here
    context = {
        'welcome_message': 'Welcome to the Journey App!',
    }
    return render(request, 'index.html', context)

@login_required
def journey_view(request):
    return render(request, 'journey.html')