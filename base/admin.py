from django.contrib import admin
from django.db.models import Count

from .models import Classroom, Student, School


class StudentInline(admin.TabularInline):
    model = Student
    extra = 2


class ClassroomInline(admin.TabularInline):
    model = Classroom
    extra = 2


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'classroom', 'school_name')
    list_filter = ('classroom', 'classroom__school')
    search_fields = ('name',)

    def school_name(self, obj):
        return obj.classroom.school.name

    school_name.admin_order_field = 'classroom__school'


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    inlines = (StudentInline,)
    list_display = ('name', 'student_count', 'school')
    search_fields = ('name',)

    def get_queryset(self, request):
        return Classroom.objects.annotate(student_count=Count('student'))

    def student_count(self, obj):
        return obj.student_set.count()

    student_count.admin_order_field = 'student_count'


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    inlines = (ClassroomInline,)
    list_display = ('name', 'classroom_count', 'student_count',)
    search_fields = ('name',)

    def get_queryset(self, request):
        return School.objects.annotate(
            student_count=Count('classroom__student'),
            classroom_count=Count('classroom')
        )

    def student_count(self, obj):
        return sum(i.student_set.count() for i in obj.classroom_set.all())

    def classroom_count(self, obj):
        return obj.classroom_set.count()

    student_count.admin_order_field = 'student_count'
    classroom_count.admin_order_field = 'classroom_count'
