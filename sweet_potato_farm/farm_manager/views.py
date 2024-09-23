from django.shortcuts import render, redirect
from .models import Harvest
from .forms import HarvestForm
import matplotlib.pyplot as plt
import io
import urllib, base64

def home(request):
    # Fetch data from the Harvest model
    harvests = Harvest.objects.all()

    # Prepare data for the chart
    labels = [harvest.date.strftime('%Y-%m-%d') for harvest in harvests]  # X-axis: Harvest dates
    values = [harvest.quantity for harvest in harvests]  # Y-axis: Harvest quantities (kg)

    # Create the bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color='#FF5733')

    plt.title('Sweet Potato Harvest in Migori')
    plt.xlabel('Date')
    plt.ylabel('Yield (kg)')
    
    # Rotate x-axis labels if there are many harvests
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a string in base64 format
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'home.html', {'data': uri})

def harvest_list(request):
    harvests = Harvest.objects.all()
    return render(request, 'harvest_list.html', {'harvests': harvests})

def add_harvest(request):
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('harvest_list')
    else:
        form = HarvestForm()
    return render(request, 'add_harvest.html', {'form': form})

