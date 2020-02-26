from django.shortcuts import render

def post_list(request):
    return render(request, 'blog1/index.html', {})
