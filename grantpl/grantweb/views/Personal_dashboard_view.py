from django.views.generic import TemplateView

class Personal_Dashboard(TemplateView):

    template_name = 'individual.html'

class Profile(TemplateView):

    template_name = 'individual_profile.html'