from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home_page.html"), name="home")
]
