from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course,Subject


# Create your views here.
def index(request):
    courses = Course.objects.order_by(
        '-created')

    subjects = Subject.objects.all()

    context = {
        'courses': courses,
        'subjects': subjects,
    } 
    return render(request, 'pages/index.html', context)


def about(request):
    """ realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    } """

    return render(request, 'pages/about.html')


def contact(request):

    return render(request, 'pages/contact-us.html')
