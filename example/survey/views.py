from django.shortcuts import render, redirect
from .forms import SignUpForm


def home_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('thank_you')

    else:
        form = SignUpForm()
    return render( request, 'home.html', {'form':form})
  
def thank_you(request):
    return render(request, 'thank_you.html')