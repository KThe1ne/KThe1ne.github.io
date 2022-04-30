from django.shortcuts import render 

storeitems = [{"type":"table","price":1000,"description":"Has four feet"},{"type":"chair","price":500,"description":"Also Has four feet"}]

def index(request):
    return render(request, "storeitems/index.html", {
        "items": storeitems
    })