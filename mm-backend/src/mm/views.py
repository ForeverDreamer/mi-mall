from django.shortcuts import render


def home_view(request):
    return render(request, "mm/home.html")


def export_view(request):
    data = {
        'ct': request.GET.get('ct'),
        'ids': request.GET.get('ids')
    }
    return render(request, "mm/export_view.html", data)
