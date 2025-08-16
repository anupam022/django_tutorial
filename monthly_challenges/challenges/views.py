from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# A dictionary to hold the challenge for each month for easy lookup.
monthly_challenges_data = {
    "january": "This works!.",
    "february": "Work for me!.",
    "march": "Solve a problem",
    "april": "Create and find a problem.",
    "may": "Learn a new skill in May!",
    "june": "Practice Django for 30 minutes every day.",
    "july": "birthday month",
    "august": "Independence day",
    "september":"Learn AWS",
    "october": "Gandhi Jayanti",
    "November": "Happy Diwali",
    "December" : "Merry Christmas"
}

# Create your views here.
def index(request):
    """Creates a list of all months with links to their challenge pages."""
    list_items = ""
    months = list(monthly_challenges_data.keys())


    for month in months:
        capitalized_month = month.capitalize()
        # Use reverse() to dynamically build the URL path
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    
    months = list(monthly_challenges_data.keys())
    if month> len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    redirect_month = months[month-1]
    return HttpResponseRedirect(reverse("month-challenge", args=[redirect_month]))


def monthly_challenge(request, month):
    """Handles the logic for a single month's challenge page."""
    try:
        challenge_text = monthly_challenges_data[month]
        return HttpResponse(f"<h1>{challenge_text}</h1>")
    except KeyError:
        # Return a 404 error if the month is not in our dictionary
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
