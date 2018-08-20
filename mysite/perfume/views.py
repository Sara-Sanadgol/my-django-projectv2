from django.shortcuts import render


def scent_list(request):
    return render(request, 'perfume.scent_list.html', {})
