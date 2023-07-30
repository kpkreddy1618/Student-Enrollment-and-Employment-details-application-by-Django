from django.shortcuts import render
from StudentApp.StudForm import StudForm,SrchForm
from StudentApp.models import Student
# Create your views here.
id=0
def menu(request):
    return render(request,'menu.html')
def register(request):
    title='New Student Registration'
    ack='Registered Successfully...'
    student=StudForm(request.POST or None)
    if request.method == 'POST':
        student=StudForm(request.POST)
        if student.is_valid():
            name=student.cleaned_data['s_name']
            clas=student.cleaned_data['s_class']
            addr=student.cleaned_data['s_address']
            school=student.cleaned_data['s_school']
            mail=student.cleaned_data['s_email']
            p=Student(s_name=name,s_class=clas,s_address=addr,s_school=school,s_email=mail)
            p.save()
            return render(request,'ack.html',{'Ack':ack})
    return render(request,'register.html',{'form':student,'title':title})
def existing(request):
    title='All Registerd Students'
    queryset=Student.objects.all()
    return render(request,'existing.html',{'title':title,'queryset':queryset})
def search(request):
    title='Search List'
    form=SrchForm(request.POST or None)
    if form.is_valid():
        gn_name=form.cleaned_data['s_name']
        queryset=Student.objects.filter(s_name=gn_name)
        if len(queryset)==0:
            return render(request,'ack.html',{'Ack':"Students not Found"})
        return render(request,'existing.html',{'queryset':queryset,'title':title})
    return render(request,'search.html',{'form':form,'title':title})
def update(request):
    
    title='Update Form'
    form=SrchForm(request.POST or None)
    if form.is_valid():
        gn_name= form.cleaned_data['s_name']
        record=Student.objects.get(s_name=gn_name)
        global id
        id=record.id
        return render(request,'update.html',{'record':record,'title':title})
    return render(request,'get.html',{'form':form,'title':title})
def updateform(request):
    record=Student.objects.get(id=id)
    name=request.POST['name']
    clas=request.POST['class']
    address=request.POST['address']
    school=request.POST['school']
    email=request.POST['email']
    record.s_name=name
    record.s_class=clas
    record.s_address=address
    record.s_school=school
    record.s_email=email
    record.save()
    return render(request,'ack.html',{'Ack':'Details Updated Successfully'})
def dropout(request):
    title='Remove Student'
    ack='Removed Successfully'
    form=SrchForm(request.POST or None)
    if form.is_valid():
        gn_name=form.cleaned_data['s_name']
        queryset=Student.objects.filter(s_name=gn_name)
        if len(queryset)==0:
            return render(request,'ack.html',{'Ack':'Students not Found'})
        else:
            queryset=Student.objects.filter(s_name=gn_name).delete()
        return render(request,'ack.html',{'Ack':ack})
    return render(request,'drop.html',{'form':form,'title':title})
