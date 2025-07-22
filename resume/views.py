from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    pojects_show=[
        {'title': 'Airbus Elevator Model',
         'image': 'images/airbus_elevator.png',
         'link' : 'https://github.com/Repcak2k1/Airbus_elevator_model'},

        {'title': 'Higher Order ODE Calculation',
         'image': 'images/ode.png',
         'link' : 'https://github.com/Repcak2k1/cs/tree/main/higher%20order%20ode%20project'},

        {'title': 'Resume Website',
         'image': 'images/website.png',
         'link' : 'https://github.com/Repcak2k1/resume'},

        {'title': 'Image Processing with Python',
         'image': 'images/image_processing.png',
         'link' : 'https://github.com/Repcak2k1/machine-learning/blob/main/image%20processing.ipynb'}
    ]
    return render(request, 'projects.html', {'projects_show': pojects_show})

def education(request):
    education=[
        {'degree': 'Aerospace Engineering',
         'institution': 'Warsaw University of Technology',
         'year': '2021 - 2025'},

        {'degree': 'Master of Electrical Engineering',
         'institution': 'Technical University of Denmark',
         'year': '2025 - ongoing'}
    ]
    return render(request, 'education.html', {'education': education})

def experience(request):
    experience=[
        {'job_title': 'Python Assistant Programmer',
         'company': 'Warsaw University of Technology',
         'year': '2021 - 2022'},

        {'job_title': 'Data Scientist',
         'company': 'VivaDrive',
         'year': '2022 - 2024'},

        {'job_title': 'Data Engineer',
         'company': 'General Electric',
         'year': '2024 - ongoing'}
    ]
    return render(request, 'experience.html', {'experience': experience})

def resume(request):
    resume_path = staticfiles_storage.path("documents/CV Kacper Pawlowski.pdf")
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment'; filename="CV_Kacper_Pawlowski.pdf"
            return response
    else:
        return HttpResponse("Resume not found.", status=404)
