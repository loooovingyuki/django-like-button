
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import LikeButtonModel

def LikePage(request, slug):
    app = LikeButtonModel.objects.get(slug=slug)
    return render(request, 'app/index.html',{"app":app})

class LikeButton(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        obj = get_object_or_404(LikeButtonModel, slug=slug)
        url_ = obj.get_absolute_url()
        status = request.GET.getlist('status')
        status = bool(int(status[0]))
        user = self.request.user
        if user in obj.like.all():
            if not(status):
                liked = True
            else:
                obj.like.remove(user)
                liked = False
        else:
            if not(status):
                liked = False
            else:
                obj.like.add(user)
                liked = True
        data = {
            "liked": liked,
        }
        return Response(data)
