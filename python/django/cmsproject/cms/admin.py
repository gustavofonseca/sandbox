from django.contrib import admin
from cms.models import Story, StoryAdmin, Category, CategoryAdmin

admin.site.register(Story, StoryAdmin)
admin.site.register(Category, CategoryAdmin)