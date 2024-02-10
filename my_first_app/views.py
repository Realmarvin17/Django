from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime


def home_view(request):
    html = f"""
    <html>
    <body>
        <h1>Welcome to my first Django site!</h1>
        <p>Today is {datetime.now().strftime('%B %d, %Y')}.</p>
        <p>This is my home page.</p>
    </body>
    </html>
    """
    # Log visit data
    with open('visits.log', 'a') as f:
        f.write(f"{datetime.now()} - Home page visited.\n")

    return HttpResponse(html)




def about_view(request):
    html = f"""
    <html>
    <body>
        <h1>About me</h1>
        <p>This is a page about myself.</p>
        <p>I am learning Django.</p>
    </body>
    </html>
    """
    # Log visit data
    with open('visits.log', 'a') as f:
        f.write(f"{datetime.now()} - About page visited.\n")

    return HttpResponse(html)