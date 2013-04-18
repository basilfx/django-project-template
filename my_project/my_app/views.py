from django.shortcuts import render, redirect

def index(request):
    return render(request, "my_app_index.html", locals())