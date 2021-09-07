from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    # return HttpResponse('Here are our projects')
    # return render(request, 'projects.html')
    # PASSING VARIABLES
    # msg = 'Hello, you are on the projects page'
    # return render(request, 'projects/projects.html', {'message': msg})
    page = 'projects'
    number = 10
    context = {'page':page, 'number': number}
    return render(request, 'projects/projects.html', context)

    # return render(request, 'projects/projects.html', {'anyname_here_to_call_in_html': msg})

def project(request, pk):
    # return HttpResponse('Single Project' + ' ' + str(pk))
    # return render(request, 'single-project.html')
    return render(request, 'projects/single-project.html')
