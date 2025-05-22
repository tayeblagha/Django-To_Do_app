from django.contrib.auth.decorators import login_required
from django.shortcuts import  render,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import  login,logout,authenticate
from todo import  models
from todo.models import TODOO
def signup(request):
    if request.method=="POST":
        fnm= request.POST.get("fnm")
        email = request.POST.get("emailid")
        password = request.POST.get("pwd")
        new_user= User.objects.create_user(fnm,email,password)
        new_user.save()
        return  redirect("/loginn")
    return render(request, 'signup.html')

def loginn(request):
    if request.method=="POST":
        fnm=request.POST.get("fnm")
        password =request.POST.get("pwd")
        is_user=authenticate(request,username=fnm,password=password)
        if is_user:
            login(request,is_user)

            return redirect("/todo")
        else:
            return redirect("/loginn")


    return render(request, 'login.html')

# @login_required(login_url='/loginn')
# def todo(request):
#     if request.method == 'POST':
#         title=request.POST.get('title')
#         print(title)
#         obj=models.TODOO(title=title,user=request.user)
#         obj.save()
#         user=request.user
#         res=models.TODOO.objects.filter(user=user).order_by('-date')
#         return redirect('/todopage',{'res':res})
#     res=models.TODOO.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'todo.html',{'res':res,})

@login_required(login_url='/loginn')
def todo(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get('title')

        new_to_do = TODOO(title=title, user=user)
        new_to_do.save()

    # Ensure this line properly gets todos ordered by date (most recent first)
    res = TODOO.objects.filter(user=user).order_by('date').reverse()
    # Render the template with context
    return render(request, "todo.html", {'res': res})


def delete_todo(request,srno):
    print(srno)
    obj=models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')

@login_required(login_url='/loginn')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        # print(title)
        obj = models.TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo')

    obj = models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})





def signout(request):
    logout(request)
    return redirect('/loginn')