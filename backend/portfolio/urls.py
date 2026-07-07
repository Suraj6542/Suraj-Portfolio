from django.urls import path
from .views import PortfolioDataView, ContactMessageView

urlpatterns = [
    path('portfolio/', PortfolioDataView.as_view(), name='portfolio-data'),
    path('contact/', ContactMessageView.as_view(), name='contact-message'),
]
