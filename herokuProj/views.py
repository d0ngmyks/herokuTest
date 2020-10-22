from django.views.generic import TemplateView

class HomepageTemplateView(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plotly_sample'] = 'SimpleExample'
        return context
