from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer

@api_view(['GET'])
# properties/views.py
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from .models import Property
from django.db.models import Avg

def property_prices_by_postcode(request):
    # Aggregate the average price for each postcode
    average_prices = Property.objects.values('postcode').annotate(average_price=Avg('price'))

    # Sort the postcodes by average price
    sorted_prices = sorted(average_prices, key=lambda x: x['average_price'], reverse=True)

    # Plotting
    postcodes = [item['postcode'] for item in sorted_prices]
    prices = [item['average_price'] for item in sorted_prices]

    plt.figure(figsize=(10, 8))
    plt.barh(postcodes, prices, color='skyblue')
    plt.xlabel('Average Price')
    plt.ylabel('Postcode')
    plt.title('Average Property Prices by Postcode')
    plt.tight_layout()

    # Save the plot to a BytesIO object and return as an image response
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type='image/png')

# Don't forget to add the corresponding URL pattern in properties/urls.py


# properties/views.py
import seaborn as sns
import pandas as pd

def heatmap_crime_price(request):
    # Fetch average crime rates by postcode
    crime_rates = CrimeData.objects.values('postcode').annotate(avg_crime_rate=Avg('crime_count'))
    crime_df = pd.DataFrame(list(crime_rates))

    # Fetch the average property prices by postcode
    property_prices = Property.objects.values('postcode').annotate(avg_price=Avg('price'))
    prices_df = pd.DataFrame(list(property_prices))

    # Merge the two DataFrames on the postcode column
    data = pd.merge(prices_df, crime_df, on='postcode')

    # Pivot the DataFrame to create a 2D array suitable for a heatmap
    pivot_table = data.pivot(index='postcode', columns='avg_crime_rate', values='avg_price')

    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_table, cmap='YlGnBu')
    plt.title('Average Property Prices by Crime Rate and Postcode')

    # Save the plot to a BytesIO object and return as an image response
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type='image/png')

def scatter_plot_property_crime(request):
    # Fetch the average crime rate by postcode
    crime_rates = CrimeData.objects.values('postcode').annotate(avg_crime_rate=Avg('crime_count'))
    crime_df = pd.DataFrame(list(crime_rates))
    
    # Fetch property prices
    property_prices = Property.objects.all().values('postcode', 'price')
    prices_df = pd.DataFrame(list(property_prices))
    
    # Convert price to numeric, assuming 'price' is stored as a string
    prices_df['price'] = pd.to_numeric(prices_df['price'], errors='coerce')
    
    # Merge the two DataFrames on the postcode column
    merged_df = pd.merge(prices_df, crime_df, on='postcode')
    
    # Plotting
    plt.figure(figsize=(10, 8))
    plt.scatter(merged_df['avg_crime_rate'], merged_df['price'])
    plt.xlabel('Average Crime Rate')
    plt.ylabel('Property Price')
    plt.title('Property Prices vs. Crime Rate')

    # Save the plot to a BytesIO object and return as an image response
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

