from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fredo Melvern Tanzil',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)