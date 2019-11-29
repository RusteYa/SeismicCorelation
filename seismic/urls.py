from django.urls import path
from django.views.generic import TemplateView

from seismic.models import Correlation

urlpatterns = [
    path('', TemplateView.as_view(template_name="seismic/main.html",
                                  extra_context={"data": Correlation.objects.all()})),
]
