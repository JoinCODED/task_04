from django.shortcuts import render
from django.views import View

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

class restaurant_list(View):    # Use class Based view 
    def get(self,request):
        context = {
            "my_list":[
                {
                    'name':'Subway',
                    'food_type':'Sandwiches.',
                },
                {
                    'name':'Steers',
                    'food_type':'Burgers, Fries, and Pasta.',
                },
                {
                    'name':'Backyard',
                    'food_type':'Been there, done that...',
                },
            ]
        }
        return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {
        "my_object":{
                        'name':'Subway',
                        'food_type':'Sandwiches.',
                    },
    }
    return render(request, 'detail.html', context)
