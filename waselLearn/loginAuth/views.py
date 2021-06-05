from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def imageView(request):

	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = UserForm()
	return render(request, 'form.html', {'form' : form})


def success(request):
    if request.method == 'GET':
        users=User.objects.all()
        return render(request, 'show.html',
                     {'allUsers' : users})

def teachers(request):
    return render(request,'teachers.html')


# def index(request):
#     if "id" in request.session:
#         return redirect('/waselApp/subjects')
#     return render(request,'index.html')

# def form(request):
#     return render(request,'form.html')

# def register(request):
#     User.objects.create(firstName=request.POST['firstName'],
#     lastName=request.POST['lastName'],
#     birthDate=request.POST['birthDate'],
#     email=request.POST['email'],
#     passwd=request.POST['passwd'],
#     mobile=request.POST['mobile'],
#     privilage=request.POST['privilage'],
#     gender=request.POST['gender'],
#     cv=request.POST['cv'],
#     location=request.POST['location'],
#     img=request.POST['img'],)
#     return redirect('/loginAuth/showAll')

# def showAll(request):
#     ccs={
#         'users':User.objects.all()
#     }
#     return render(request, "show.html",ccs)







# def loginOrRegister(request):
#     if (request.method=="POST") and (request.POST['regesterOrLogin']=="register"):
#         errors = User.objects.isValid(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/')
#         else:

#             hashedPasswd=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            
#             User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],birthDate=request.POST['bday'],email=request.POST['email'],passwd=hashedPasswd)
#             request.session['logedin']=True
#             request.session['email'] = request.POST['email']
#             thisUser=User.objects.get(email=request.POST['email'])
#             request.session['id']=thisUser.id
#             request.session['thisUsersName']=thisUser.fname
#             return redirect('/thoughts')

#     elif (request.method=="POST" and request.POST['regesterOrLogin']=="login"):
#         errors = User.objects.loginValid(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/')
#         else:
#             one=request.POST['email']
#             two=request.POST['password']
#             try:
#                 users = User.objects.filter(email=one)
#                 thisUser = users[0]
#             except:
#                 messages.error(request, "this email doesn't exist")
#                 return redirect('/')
#             if bcrypt.checkpw(two.encode(),thisUser.passwd.encode()):
#                 request.session['id']=thisUser.id
#                 request.session['logedin']=True
#                 request.session['thisUsersName']=one
#                 request.session['email']=one
#                 return redirect('/thoughts')
#             else:
#                 messages.error(request, "I have this email but the password is NOT right")
#                 return redirect('/')
#     return redirect('/')