from django.shortcuts import render
from src.personal.models import Questions
from src.account.models import Account

# Create your views here.

def home_screen_view(request):
    context = {}
    # context['some_string'] = "variable"

    # context = {
    #     'some_string': "varibale",
    # }
    #
    # list_of_values = []
    # list_of_values.append("first")
    # list_of_values.append("second")
    # list_of_values.append("third")
    # context['list_of_values'] = list_of_values
    #
    # questions = Questions.objects.all()
    # context['questions'] = questions

    context['accounts'] = Account.object.all()

    return render(request, "personal/home.html", context)
