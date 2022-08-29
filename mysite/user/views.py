from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile


def index(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES) # Gets the uploaded data and maps it to the ProfileForm object
		if form.is_valid(): # Checks if the uploaded data is valid or not
			form.save() # Saves the uploaded data into our Database model
			return redirect('home') # Makes the page redirect back to home
    
	else:
		form = ProfileForm()
    
	posts = Profile.objects.all().order_by('-date_posted') # Fetched all the data from database model in the dec order of date_posted field
	return render(request, 'user/home.html', {'form' : form, 'posts':posts}) # Return the home.html page having form and userData passed as a dictionary
