from django.shortcuts import render

def post_list(request):
    if request.method == 'GET':
        return render(request, 'blog1/index.html')
