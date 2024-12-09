from django.shortcuts import redirect, HttpResponse,render
from django.template import loader
from .models import Task


# Create your views here.
def get_tasks(request):
    tasks = Task.objects.all().values()
    template = loader.get_template("todo/tasks.html")
    context = {"tasks": tasks}
    return HttpResponse(template.render(context=context, request=request))


def add_task(request):
    if request.method == "POST":
        Task.objects.create(Title=request.POST.get("title"))
        return redirect("/todo/")
    
    return render(request, "todo/create.html")


def IndexPage(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render(request=request))
