from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import localtime, strftime
from .models import *

def home(request):
    return render(request,'home.html')

def subjects(request):
    return render(request,'subjects.html')
def about(request):
    return render(request,'about.html')

def allTeachers(request):
    return render(request,'allTeachers.html')

def teachers(request):
    context={
        'allUsers' : User.objects.filter(privilage=7),
    }
    return render(request,"teachers.html",context)

def teachersBiology(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="biology"),
    }
    return render(request,"teachers.html",context)
def teachersphysics(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="physics"),
    }
    return render(request,"teachers.html",context)
def teacherschemistry(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="chemistry"),
    }
    return render(request,"teachers.html",context)
def teachersenglish(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="english"),
    }
    return render(request,"teachers.html",context)
def teachersmathematics(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="mathematics"),
    }
    return render(request,"teachers.html",context)
def teachersarabic(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="arabic"),
    }
    return render(request,"teachers.html",context)
def teachersart(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="art"),
    }
    return render(request,"teachers.html",context)
def teachersmusic(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="music"),
    }
    return render(request,"teachers.html",context)
def teachershistory(request):
    context={
        'allUsers' : User.objects.filter(privilage=7, course="history"),
    }
    return render(request,"teachers.html",context)

def suggest(request):
    Sugestion.objects.create(title=request.POST['title'],fullName=request.POST['name'],email=request.POST['email'],description=request.POST['message'])
    return redirect('/')

def teacher(request,teacherId):
    todayTime= strftime("%Y-%B-%A", localtime())
    todayTimeList = todayTime.split("-")
    context={
		'teacher' : User.objects.get(id=teacherId),
		'times' : todayTimeList,
        'n' : range(9) 
	}
    return render(request,"teacher.html",context)




# def welcomeThoughts(request):
#     if request.session['logedin']:
#         thisUsers= User.objects.get(email=request.session['email'])
#         request.session['thisUsersName']=thisUsers.fname
#         request.session['id']=thisUsers.id
#         request.session['thisUsersLname']=thisUsers.lname
#         allThoughts = Thought.objects.all()
#         #allThoughts = allThoughts.order_by('likedBy').reverse()
#         context={
#             'Thoughts' : allThoughts,
#             'hisFavs' : Thought.objects.filter(likedBy=thisUsers),
#         }
#         return render(request,'thoughts.html', context)

# def thoughtData(request, id):
#     if request.session['logedin']:
#         thisUsers= User.objects.get(email=request.session['email'])
#         thisThought = Thought.objects.get(id=id),
#         thisThought = thisThought[0]
#         q1 = User.objects.filter(likes=thisThought.id)
#         notAllLikers = q1.exclude(createdThoughts=thisThought)
#         context={
#             'specificThought' : Thought.objects.get(id=id),
#             'hisFavs' : Thought.objects.filter(likedBy=thisUsers),
#             'likers' : notAllLikers
#         }
#         return render(request,'specificThought.html', context)

# def deleteThought(request, id):
#     delThought(id)
#     return redirect('/')

# def addThought(request):
#     desc = request.POST['formDesc']
#     userId = request.session['id']
#     createThought(desc, userId)
#     return redirect('/')

# def likeThought(request, id):
#     userId = request.session['id']
#     likeSomeThought(id, userId)
#     return redirect('/')

# def unlikethisThought(request, id):
#     userId = request.session['id']
#     unlikeSomeThought(id, userId)
#     return redirect('/')

def cleanTheSession(request):
    request.session.clear()
    return redirect('/')

# def autocomplete(request, str): 
#     data={}    
#     x=User.objects.filter(first_name__contains=str)  
#     names=[]    
#     for i in x:       
#         names.append('<div>' + i.first_name + '</div>')       
#     data['names'] = names   
#     return JsonResponse(data)    

def autocomplete(request, str): 
    data={}     
    x=User.objects.filter(firstName__contains=str)
    names=[]     
    for i in x:         
        names.append(i.firstName )     
        data['names'] = names
    return JsonResponse(data)

def new(request):
    return render(request, 'new.html')
