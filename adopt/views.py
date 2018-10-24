from django.shortcuts import render
from .forms import PerritoForm
from django.shortcuts import redirect



def newperrito(request):
    if request.method == "POST":
        form = PerritoForm(request.POST, request.FILES)
        if form.is_valid():
            Perrito = form.save(commit=True)
            Perrito.save()
            return redirect('thanks')
    else:
        form = PerritoForm()
    return render(request, 'core/new-perrito.html', {'form': form})
