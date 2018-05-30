from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from .forms import QuestionsForm, QuestionpaperForm, StudentForm
from .models import Questions, Questionpaper, Student
from django.contrib.auth.decorators import login_required


def RegisterStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            student.refresh_from_db()  # load the profile instance created by the signal
            student.student.school = form.cleaned_data.get('school')
            student.student.gender = form.cleaned_data.get('gender')
            student.student.dob = form.cleaned_data.get('dob')
            student.student.phone = form.cleaned_data.get('phone')
            student.student.is_student = True
            student.save()
            return redirect('login')
    else:
        form = StudentForm()
    return render(request, 'registration/student_register.html',{'form':form})


def verify(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method=='POST':
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            query = Student.objects.filter(user=user).get().is_student
            if user.is_superuser:
                return redirect('admin_home')
            elif query is False and user.is_staff is True:
                return redirect('teacher_home')
            elif query is True:
                return redirect('student_home')
            else:
                return redirect('login')
        else:
            return render(request,'registration/login.html',{'username':username, 'message':'Incorrect Username/Password'})
    else:
        return render(request,'registration/login.html', {'': ''})


@login_required(login_url='login')
def student_home(request):
    return render(request, 'student_home.html', {'': ''})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def question_list(request):
    questions = Questions.objects.all()
    return render(request,'questions/question_list.html',{'questions':questions})

@login_required
def question_new(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('question_list')
    else:
        form = QuestionsForm()
    return render(request, 'questions/question_edit.html',{'form':form})

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Questions, pk=pk)
    return render(request, 'questions/question_detail.html', {'question': question})


def paper_new(request):
    form = QuestionpaperForm(request.POST)
    if form.is_valid():
        paper = form.save(commit=False)
        paper.save()
        return redirect('paper_new')
    else:
        form = QuestionpaperForm()
    return render(request, 'question_paper/paper_new.html',{'form':form})

def get_question_list(subject, klass):
    question_l = Questions.objects.filter(subject=subject).filter(klass=klass)
    return question_l

def test_generator(request):
    subjects = Questions.SUBJECT_LIST
    klass = Questions.KLASS_LIST
    if request.method == 'POST':
        subject = request.POST.get('subject')
        student_klass = request.POST.get('student_class')
        question_list = get_question_list(subject, student_klass)


    context = {'subjects': subjects,
               'classes': klass}
    return render(request, 'question_paper/test_generator.html', context=context)