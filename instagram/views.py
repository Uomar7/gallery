from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,category,Location

def all_images(request):
    images = Image.all_images()
    return render(request, 'all-out/index.html', {"images":images})

def images_of_the_day(request):
    date = dt.date.today()
    images = Image.todays_images()
    return render(request, 'all-out/today-pics.html', {"date":date, "images": images})

def past_images(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_the_day)
    
    images = Image.days_images(date)
    return render(request, 'all-out/past-pics.html', {"date":date, "images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        
        term_cat = category.objects.all()
        print(term_cat)
        for i in term_cat:
            if i.name == search_term:            
                searched_images = Image.search_by_category(i.id)
                
        message = f"{search_term}"

        return render(request, 'all-out/search.html', {"message":message, "images":searched_images})

    else:
        message = "You Haven't Searched For Any Term"

        return render(request, 'all-out/search.html', {"message":message})
