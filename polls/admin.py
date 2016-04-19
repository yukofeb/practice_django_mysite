from django.contrib import admin
from polls.models import Poll, Choice


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'pub_date', 'was_published_recently')
    list_display_links = ('id', 'question')
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    #date_hierarchy = 'pub_date'
admin.site.register(Poll, PollAdmin)


#class ChoiceAdmin(admin.ModelAdmin):
#    list_display = ('id', 'poll', 'choice', 'votes')
#    list_display_links = ('id', 'poll')
#admin.site.register(Choice, ChoiceAdmin)
