from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MilestoneCustomizationForm
from .models import Milestone, Tag

def index_view(request):
    # Add any context data you want to pass to the template here
    context = {
        'welcome_message': 'Welcome to the Journey App!',
    }
    return render(request, 'index.html', context)

@login_required
def journey_view(request):
    user = request.user  # Get the current logged-in user
    
    # Query the Milestone model to get user-specific data
    user_milestones = Milestone.objects.filter(user=user)
    
    context = {
        'user_milestones': user_milestones,  # Pass the data to the template
    }
    return render(request, 'journey.html', context)

@login_required
def create_milestone_view(request):
    if request.method == 'POST':
        form = MilestoneCustomizationForm(request.POST)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.user = request.user
            milestone.save()

            # Process and save tags
            tags = form.cleaned_data['tags']
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())  # Create or retrieve the tag
                milestone.tags.add(tag)  # Associate the tag with the milestone

            return redirect('journey')  # Redirect to the journey page after creating the milestone
    else:
        form = MilestoneCustomizationForm()

    context = {
        'form': form,
    }
    return render(request, 'create_milestone.html', context)

@login_required
def customize_milestone_view(request, milestone_id):
    milestone = Milestone.objects.get(pk=milestone_id, user=request.user)

    if request.method == 'POST':
        form = MilestoneCustomizationForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('journey')  # Redirect to the journey page after customization
    else:
        form = MilestoneCustomizationForm(instance=milestone)

    context = {
        'form': form,
        'milestone': milestone,
    }
    return render(request, 'customize_milestone.html', context)
