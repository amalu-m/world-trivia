from django.contrib import admin
from problems.models import Country, Question, Answer

# Register your models here.

admin.site.register(Country)
admin.site.register(Question)
admin.site.register(Answer)
