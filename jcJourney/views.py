from django.shortcuts import render
from django.views.generic import TemplateView
from .models import LearningJourney, AboutMe, AdminScreenshots

class IndexView(TemplateView):
    """
    Home page view displaying Jigme Choden's learning journey
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['learning_items'] = LearningJourney.objects.all().order_by('-date_learned')
        context['about_me'] = AboutMe.objects.first()
        context['screenshots'] = AdminScreenshots.objects.all().order_by('display_order')  # ADD THIS LINE
        return context

class AboutMeView(TemplateView):
    """
    About Me page view displaying personal information
    """
    template_name = 'aboutMe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_me = AboutMe.objects.first()
        context['about_me'] = about_me
        if about_me:
            context['interests_list'] = [interest.strip() for interest in about_me.interests.split(',')]
            context['skills_list'] = [skill.strip() for skill in about_me.skills.split(',')]
        return context

class AdminInterfaceView(TemplateView):
    """
    Admin Interface page view displaying screenshots
    """
    template_name = 'admin_interface.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['screenshots'] = AdminScreenshots.objects.all().order_by('display_order')
        return context