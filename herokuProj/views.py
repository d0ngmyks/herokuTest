from django.views.generic import TemplateView

class HomepageTemplateView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['developer'] = 'DOOOOOOOONG'
        return context