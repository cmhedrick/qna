from django.contrib import admin

from qna_app import models

admin.site.register(models.Organization)
admin.site.register(models.Staff)
admin.site.register(models.Role)
admin.site.register(models.Question)
