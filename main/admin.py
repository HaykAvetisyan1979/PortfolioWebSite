from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

admin.site.register(Tag)

@admin.register(Me)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

@admin.register(Blog)
class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ["title" , 'text']



@admin.register(AboutMe)
class AboutMeModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ['text']

@admin.register(WhatIDo)
class WhatIDoModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(Testimonials)
class TestimonialsModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']

@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['url', 'logo']

@admin.register(FunFacts)
class FunFactsModelAdmin(admin.ModelAdmin):
    list_display = ["happy_clients", "working_hours", "awards_won"]

@admin.register(Education)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ["specialization"]

@admin.register(SkillType)
class SkillTypeModelAdmin(admin.ModelAdmin):
    list_display = ["type"]

@admin.register(Skill)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ["skill_name"]

@admin.register(Knowledges)
class KnowledgesModelAdmin(admin.ModelAdmin):
    list_display = ["knowledge"]

@admin.register(WorkingExperience)
class WorkingExperienceModelAdmin(admin.ModelAdmin):
    list_display = ["role"]

@admin.register(Certificates)
class CertificatesModelAdmin(admin.ModelAdmin):
    list_display = ["membership_id"]

@admin.register(PortfolioCategory)
class PortfolioCategorysModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(PortfolioItems)
class PortfolioItemsModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
