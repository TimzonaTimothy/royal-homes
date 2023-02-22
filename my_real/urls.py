from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings', views.listings, name='listings'),
    path('listings/<int:listing_id>', views.listing, name='listing'),
    path('contact', views.contact, name='contact'),
    path('contact_us', views.main_contact, name='contact_us'),
    path('about', views.about, name='about'),
    # path('agent', views.agent, name='agent'),
    path('search', views.search, name='search'),
]