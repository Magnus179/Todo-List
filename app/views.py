from django.shortcuts import render , redirect
from .models import Todo,History
# Create your views here.
def home(request):
    data = Todo.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        create = Todo.objects.create(task = task , description = description)
    context = {'data':data}
    return render(request,'home.html',context)

def alltodos(request):
    update = True
    data1 = Todo.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        data1 = Todo.objects.filter(task__icontains=search)
        print(search)
    context = {
        'data' : data1,
        'update' : update
    }
    return render(request,'alltodos.html',context)

def todolists(request,pk):
    data2 = Todo.objects.get(id = pk)
    if request.method == 'POST':
        History.objects.create(new_task = data2.task,desc=data2.description)
        data2.delete()
        return redirect('home')
    context = {
        'data' : data2
    }
    return render(request,'todolists.html',context)

def edit(request,pk):
    data3 = Todo.objects.get(id=pk)
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        data3.task = task
        data3.description = description
        data3.save()
        return redirect('alltodos')
    
    context = {
        'data' : data3
    }
    return render(request,'edit.html',context)
def list(req):
    update = True
    list = History.objects.all()
    if req.method == 'POST':
        id = req.POST.get('id')
        if id:
            list1  = History.objects.get(id=id)
            print(id)
            list1.delete()
            return redirect('home')
        search = req.POST.get('search')
        if search:
                 list= History.objects.filter(new_task__icontains=search)
        print(search)
    context = {
        'list':list,
        'update' : update

    }
    return render(req,'histroy.html',context)
