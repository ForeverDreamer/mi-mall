from django.shortcuts import render


def export_view(request):
    data = {
        'ct': request.GET.get('ct'),
        'ids': request.GET.get('ids')
    }
    return render(request, "common/export_view.html", data)
