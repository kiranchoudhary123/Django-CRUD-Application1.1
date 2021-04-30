from django.shortcuts import render,redirect
from .forms import StudentRegidtration
from .forms import User

# Create your views here.
def base(request):
    if request.method == "POST":
        form = StudentRegidtration(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentRegidtration()
    return render(request,'enroll/base.html',{'form':form})
# this function will add ew items and show items.
def show(request):
    if request.method == 'POST':
        fm = StudentRegidtration(request.POST)
        if fm.is_valid():

            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            con=fm.cleaned_data['contact']
            reg = User(name=nm,email=em,password=pw,contact=con)
            reg.save()
            fm = StudentRegidtration()

    else:
        fm = StudentRegidtration()
    stud = User.objects.all()
    return render(request,'enroll/show.html',{'form':fm,'stu':stud})
#this function will update/redirect
def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        fm = StudentRegidtration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/show/')
    else:
        pi = User.objects.get(id=id)
        fm = StudentRegidtration(instance=pi)

    return render(request, 'enroll/update.html', {'form':fm})

    #this function will Delete
def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        pi.delete()
        return redirect('/show/')
    return render(request, 'enroll/info.html')
