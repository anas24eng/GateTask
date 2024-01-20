from django.shortcuts import render

from rec.forms import RecruitmentForm


def index(request):
    form = RecruitmentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        cv_type = form.cleaned_data['cv'].content_type
        if cv_type == 'application/pdf':
            form.save()

    return render(request, 'rec/index.html', {'form': form})