from django.shortcuts import render


@login_required
def homepage(request):
    return render(request, "index.html")