from django.contrib import admin

from board.models import Repository, Introduction, Comment

admin.site.register(Repository)
admin.site.register(Introduction)
admin.site.register(Comment)
