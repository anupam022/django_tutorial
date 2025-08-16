from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

# A dictionary to hold the challenge for each month for easy lookup.
monthly_challenges_data = {
    "january": "This works!.",
    "february": "Work for me!.",
    "march": "Solve a problem",
    "april": "Create and find a problem.",
    "may": "Learn a new skill in May!",
    "june": "Practice Django for 30 minutes every day.",
    "july": None,
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

    return render(request, "challenges\index.html",{
        "months":months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     # Use reverse() to dynamically build the URL path
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

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
        return render(request, "challenges/challenge.html",{
            "text":challenge_text,
            "month_name": month.capitalize()
        }) #This will work same as below code 
        # {
        #         "text":challenge_text     Context param we can pass multiple context and use in html file
        #     }
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except KeyError:
        # Return a 404 error if the month is not in our dictionary
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404("We could not found page!")
