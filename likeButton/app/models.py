from django.db import models
from django.urls import reverse
from django.conf import settings

class LikeButtonModel(models.Model):
    # ユーザー情報
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title    = models.CharField(max_length=100)
    slug     = models.SlugField()
    body     = models.TextField()
    date     = models.DateTimeField(auto_now_add=True)
    thumb    = models.ImageField(default='default.png', blank=True)
    like     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")

    def get_absolute_url(self):
        return reverse("app:like_page", kwargs={"slug": self.slug})

    def get_api_like_url(self):
        return reverse("app:like_api", kwargs={"slug": self.slug})
