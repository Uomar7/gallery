from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

def images_of_the_day(request):
    date = dt.date.today()
   
    return render(request, 'all-out/today-pics.html', {"date":date})

def past_images(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    if date == dt.date.today():
        return redirect(images_of_the_day)

    return render(request, 'all-out/past-pics.html', {"date":date})