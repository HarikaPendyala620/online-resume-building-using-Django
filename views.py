from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm

def home(request):
    return render(request, 'index.html')

def gen_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_detail')
    else:
        form = ResumeForm()
    return render(request, 'gen_resume.html', {'form': form})

def resume_detail(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_detail.html', {'resumes': resumes})