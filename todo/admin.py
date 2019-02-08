from django.contrib import admin
from .models import Todo, Checklist, Attachments
from .forms import TodoForm

class ChecklistInline(admin.TabularInline):
    model = Todo.checklist.through
    extra = 2


class ChecklistStackInline(admin.StackedInline):
    model = Todo.checklist.through


class ChecklistAdmin(admin.ModelAdmin):
     inlines = [
         ChecklistInline,
     ]

class TodoAdmin(admin.ModelAdmin):
    ordering = ['date_created']
    list_display = ('id', 'content', 'user', 'done', 'checklist_count')
    list_display_links = ('content',)
    inlines = [ChecklistStackInline,]
    exclude = ('checklist', 'user',)
    form = TodoForm

    def save_model(self, request, obj, form, change):
        # override save method
        # auto save user/hides user selection to admin form
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Attachments)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Checklist, ChecklistAdmin)