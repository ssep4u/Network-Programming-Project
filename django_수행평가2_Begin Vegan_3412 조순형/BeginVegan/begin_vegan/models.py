from django.db import models

from accounts.models import Profile


class Post(models.Model):
    ALL = '전체'
    VEGAN = '비건'
    LACTO_OVO = '락토-오보'
    PESCO = '페스코'
    POLLO = '폴로'
    FLEXITARIAN = '플렉시테리언'

    TENDENCY = [
        (ALL, '전체'),
        (VEGAN, '비건'),
        (LACTO_OVO, '락토-오보'),
        (PESCO, '페스코'),
        (POLLO, '폴로'),
        (FLEXITARIAN, '플렉시테리언'),
    ]

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=6, choices=TENDENCY, default=FLEXITARIAN)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Comments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
