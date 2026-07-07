from django.contrib import admin
from .models import (
    Profile, SkillCategory, Skill, Experience, ExperienceBullet,
    Project, ProjectBullet, Education, Leadership, LeadershipBullet,
    Award, ContactMessage,
)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1


class ProjectBulletInline(admin.TabularInline):
    model = ProjectBullet
    extra = 1


class LeadershipBulletInline(admin.TabularInline):
    model = LeadershipBullet
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'location']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    inlines = [SkillInline]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'role', 'start_date', 'end_date']
    inlines = [ExperienceBulletInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tech_stack']
    inlines = [ProjectBulletInline]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_year', 'end_year']


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ['organization', 'role', 'start_date', 'end_date']
    inlines = [LeadershipBulletInline]


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
