from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # repo1.introduction_set
    class Meta:
        verbose_name_plural = 'Repositories'
        ordering = ['deadline']

    def __str__(self):
        return self.name


class Introduction(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)  # intro1.repository
    title = models.CharField(max_length=30)
    number = models.IntegerField(default=1)
    contents = models.TextField(max_length=300)
    writer = models.CharField(max_length=10)

    # intro1.comment_set
    class Meta:
        ordering = ['-number']

    def __str__(self):
        return f'{self.number} {self.contents}'


class Comment(models.Model):
    text = models.ForeignKey(Introduction, on_delete=models.CASCADE)  # comm1.introduction
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment
