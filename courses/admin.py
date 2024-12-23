from django.contrib import admin
from .models import Subject, Course, Module, Content

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(Content)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['module', 'content_type',]

# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'
