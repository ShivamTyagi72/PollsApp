from django.contrib import admin

# Register your models here.

from .models import Question,choice 

class choiceinline(admin.TabularInline):
    model=choice
    extra=3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,   {'fields':['question_text']}),
    ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[choiceinline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']



admin.site.register(Question,QuestionAdmin)
admin.site.register(choice)
