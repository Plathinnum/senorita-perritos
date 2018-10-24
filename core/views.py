from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect

def home(request):
    return render(request, 'core/home.html')

def thanks(request):
    return render(request, 'core/thanks.html')

def form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contacto = form.save(commit=True)
            Contacto.save()
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'core/form.html', {'form': form})