# property/urls.py
from django.urls import path
from .views import properties_by_postcode
# properties/urls.py
from . import views


urlpatterns = [
    path('properties/', properties_by_postcode, name='properties-by-postcode'),


    # URL pattern for the property prices by postcode visualization
    path('visualizations/property-prices-by-postcode/', views.property_prices_by_postcode, name='property_prices_by_postcode'),

    # URL pattern for the crime rate heatmap visualization
    path('visualizations/heatmap-crime-rate/', views.heatmap_crime_price, name='heatmap_crime_price'),

    # URL pattern for the property prices vs. crime rate scatter plot visualization
    path('visualizations/property-crime-scatter/', views.scatter_plot_property_crime, name='scatter_plot_property_crime'),

    # will more patterns for other visualizations here
]

