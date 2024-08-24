from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.core.mail import send_mail
from Portfolio.settings import EMAIL_HOST_USER, EMAIL_SUPPORT_USER
from .models import (
    Me, AboutMe, WhatIDo, Testimonials, Client, FunFacts, 
    Education, SkillType, Skill, WorkingExperience, Certificates, 
    Knowledges, PortfolioItems, PortfolioCategory, Blog
)
from .forms import ContactForm



class HomeListView(ListView):
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data():

        user_object = Me.objects.first()
        about_me = AboutMe.objects.first()
        services = WhatIDo.objects.all()
        testimonials = Testimonials.objects.all()
        client = Client.objects.all()
        fun_facts = FunFacts.objects.first()
        educations = Education.objects.all()
        skill_type = SkillType.objects.all()
        skills = Skill.objects.all()
        experiances = WorkingExperience.objects.all()
        certificates = Certificates.objects.all()
        knowledges = Knowledges.objects.all()
        portfolio_category = PortfolioCategory.objects.all()
        portfolio_items = PortfolioItems.objects.all()
        blogs = Blog.objects.all()

        context = {
            'user_object':user_object,
            'about_me': about_me,
            'services_1':services[:2],
            'services_2':services[2:],
            'testimonials':testimonials,
            'clients':client,
            'fun_facts':fun_facts,
            'educations':educations,
            'skill_type':skill_type,
            'skills':skills,
            'experiances':experiances,
            'certificates':certificates,
            'knowledges':knowledges,
            'portfolio_category':portfolio_category,
            'portfolio_items':portfolio_items,
            'blog_1':blogs[:2],
            'blog_2':blogs[2:],

        }

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context=self.__extract_all_data())
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            
            email_massage = f"Sender Name: {full_name}\nSender Email: {email}\nTopic: {subject}\nMessage:\n{message}"
            send_mail(
                subject="Message From Portfolio",
                message=email_massage,
                recipient_list=[EMAIL_SUPPORT_USER],
                from_email=EMAIL_HOST_USER
            )
            form.save()
        else:
            form = ContactForm()
        
        return redirect('/')



class BlogPost1View(TemplateView):
    template_name = 'blog-post-1.html'

    @staticmethod
    def __extract_all_data():
        user_object = Me.objects.first()

        context = {
            'user_object':user_object,
        }
        return  context
    
    def get(self, request: HttpRequest, blog_id, *args: Any, **kwargs: Any) -> HttpResponse:
        blog = Blog.objects.get(id=blog_id)

        context = self.__extract_all_data()
        context.update({
            'blog': blog,
        })
        return render(request, self.template_name, context=context)
    