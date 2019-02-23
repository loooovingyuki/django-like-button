
from django.http import HttpResponse
from django.shortcuts import render

def LikeButton(request):
    return render(request, 'app/like-button.html')
