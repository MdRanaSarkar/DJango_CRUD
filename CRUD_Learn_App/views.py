from django.shortcuts import render, redirect, get_object_or_404
from .form import Student_admission_form
from .models import Student_Admission, Item
# Create your views here.Item


def index(request):
    item = Item.objects.all()
    context = {'item': item}
    return render(request, 'index.html', context)


def student_admission(request):
    form = Student_admission_form(request.POST, request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('main')

    context = {'form': form}
    return render(request, 'student_admission_form.html', context)


def student_list(request):
    data = Student_Admission.objects.all()
    context = {'data': data}
    return render(request, 'student_list.html', context)


def Student_details(request, id):
    data = Student_Admission.objects.get(id=id)
    context = {'data': data}
    return render(request, 'student_details.html', context)


def student_update(request, id):
    data = Student_Admission.objects.get(id=id)
    form = Student_admission_form(request.POST or None, instance=data)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('student_list')

    context = {'form': form}
    return render(request, 'student_admission_form.html', context)


def Student_delete(request, id):
    data = Student_Admission.objects.get(id=id)
    data.delete()
    return redirect('student_list')
