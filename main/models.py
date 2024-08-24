from typing import Iterable
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import mark_safe, format_html
from typing import Iterable, Optional

class Me(models.Model):
    image = models.ImageField(_("Profile Image"), upload_to='profile_images/')

    name = models.CharField(_('Name'), max_length=255)
    surname = models.CharField(_('Surname'), max_length=255)
    age = models.PositiveSmallIntegerField(_("Age"))
    residence = models.CharField(_('Residence'), max_length=100)
    address  = models.CharField(_('Address '), max_length=100)
    email = models.EmailField(_("Email"))
    phone = PhoneNumberField(verbose_name=_("Phone Number with country code"))

    profession = models.CharField(_('Profession'), max_length=255)

    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    cv_file = models.FileField(upload_to='cvs/')

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        if self.pk is None:  # New instance
            if Me.objects.exists():
                raise ValidationError('There can only be one instance of the Me model.')
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = _('Me')
        verbose_name_plural = _('Me')



class ContactWithMe(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Message"))

    def __str__(self) -> str:
        return self.subject
    
    class Meta:
        verbose_name = _('Contact With Me')
        verbose_name_plural = _('Contact With Me')


class AboutMe(models.Model):
    text = models.TextField("About Me")

    # def __str__(self) -> str:
    #     return self.text[:50].replace('<p>' , '').replace("</p>", "")
    
    class Meta:
        verbose_name = _('About Me')
        verbose_name_plural = _('About Me')


class WhatIDo(models.Model):
    icon = models.CharField(_('Icon'), max_length=255)
    title = models.CharField(_("Topic"), max_length=100)
    text = models.TextField(_("About Experiance"))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('What I Do')
        verbose_name_plural = _('What I Do')
 


class Testimonials(models.Model):
    image = models.ImageField(_("Image"), upload_to='testimonials/')
    text = models.TextField(_("About Worker"))
    full_name = models.CharField(_("Full Name"), max_length=255)
    company_name = models.CharField(_("Company Name"), max_length=255)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('Testimonials')
        verbose_name_plural = _('Testimonials')
 

class Client(models.Model):
    logo = models.ImageField(_("Logo"))
    url = models.URLField(_("Client Website or Project URL"))

    def __str__(self) -> str:
        return self.url
    
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Client')
 


class FunFacts(models.Model):
    happy_clients = models.PositiveIntegerField(_("Happy Clients"))
    working_hours = models.PositiveIntegerField(_("Working Hours"))
    awards_won = models.PositiveIntegerField(_("Awards Won"))

    def __str__(self) -> str:
        return "Facts"
    
    class Meta:
        verbose_name = _('Fun Fact')
        verbose_name_plural = _('Fun Facts')
 

class Education(models.Model):
    year = models.PositiveSmallIntegerField(_("Graduation Year"))
    institution = models.CharField(_("institution"), max_length=255)
    specialization = models.CharField(_("specialization"), max_length=255)
    about = models.TextField(_("About(skills and etc.)"))

    def __str__(self) -> str:
        return self.institution

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')

class SkillType(models.Model):
    type = models.CharField(_("Skill Type(Coding, Design and etc.)"), max_length=50)

    def __str__(self) -> str:
        return self.type

    class Meta:
        verbose_name = _('Skill Type')
        verbose_name_plural = _('Skill Types')


class Skill(models.Model):
    skill_type = models.ForeignKey("SkillType", on_delete=models.PROTECT, related_name="sk_type")
    skill_name = models.CharField(_("Skill"), max_length=255)
    level = models.DecimalField(_("Level With Percentage"),max_digits=2, decimal_places=0)


    def save(self, force_insert: bool = False, force_update: bool = False, using: Optional[str] = None, update_fields: Optional[Iterable[str]] = None) -> None:
        # Ensure 'level' is an integer
        if self.level is not None:
            self.level = int(self.level)
        
        # Call the parent class's save method
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')


class Knowledges(models.Model):
    knowledge = models.CharField(_("Knowledge"), max_length=255)

    def __str__(self) -> str:
        return self.knowledge
    
    class Meta:
        verbose_name = _('Knowledge')
        verbose_name_plural = _('Knowledges')

class WorkingExperience(models.Model):
    start_year = models.DateField(_("Start Year"))
    end_year = models.DateField(_("End Year"))
    company = models.CharField(_("Company"),max_length=255)
    role = models.CharField(_("Role"), max_length=255)
    text = models.TextField(_("About company and your role in it."))

    def save(self, force_insert: bool = False, force_update: bool = False, using: Optional[str] = None, update_fields: Optional[Iterable[str]] = None) -> None:
        # Format date fields
        if self.start_year:
            self.start_year = self.start_year.strftime('%Y%m%d')
        if self.end_year:
            self.end_year = self.end_year.strftime('%Y%m%d')

        # Call the parent class's save method
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    def __str__(self) -> str:
        return self.company
    
    class Meta:
        verbose_name = _('Working Experience')
        verbose_name_plural = _('Working Experience')


class Certificates(models.Model):
    logo = models.ImageField(_('Certificates'), upload_to='certificates/')
    certification = models.CharField(_('certification'), max_length=255)
    membership_id = models.CharField(_("Membership ID"), max_length=255)

    date = models.DateField(_("Certification Date"))

    def __str__(self) -> str:
        return self.certification

    class Meta:
        verbose_name = _('Certificate')
        verbose_name_plural = _('Certificates')

class PortfolioCategory(models.Model):
    
    name = models.CharField(_('Portfolio Category'), max_length=255)

    def __str__(self) -> str:
        return self.name
    
    
    class Meta:
        verbose_name = _('Portfolio Category')
        verbose_name_plural = _('Portfolio Categories')

class PortfolioItems(models.Model):
    category = models.ForeignKey("PortfolioCategory", on_delete=models.CASCADE, related_name='portfolio_categ')
    image = models.ImageField()
    media = models.FileField(_("Media file, or full size file"), upload_to='portfolioItems/')
    title = models.CharField(_('Title'), max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Portfolio Item')
        verbose_name_plural = _('Portfolio Items')


class Tag(models.Model):
    name = models.CharField(_("Tag"), max_length=155)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

class Blog(models.Model):
    image = models.ImageField(_('Image'), upload_to='blog/') 
    image_full = models.ImageField(_("Image Full"), upload_to="blog/full/")
    main_tag = models.CharField(_("Main Tag"), max_length=15)
    title = models.CharField(_('Title'), max_length=255, default='default_title_class')
    text = models.TextField(_("Text"))
    date = models.DateField(_("Creation Day"))
    author = models.CharField(_("Author"), max_length=50)

    facebook = models.URLField(_("Facebook"))
    twitter = models.URLField(_("Twitter"))
    linkedin = models.URLField(_("Linkedin"))

    tags = models.ManyToManyField("Tag")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')



