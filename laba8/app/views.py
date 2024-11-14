from django.shortcuts import render
from .models import Error, Programmer, ErrorFix

def project_info(request):
    errors = Error.objects.all()
    programmers = Programmer.objects.all()
    error_fixes = ErrorFix.objects.all()

    # Передаем данные в шаблон
    return render(request, 'project_info.html', {
        'project_name': 'Лабораторна робота №8',  
        'student_name': 'Матвєєв Ярослав Дмитрович',
        'student_group': 'КБ21015Б',
        'errors': errors,
        'programmers': programmers,
        'error_fixes': error_fixes,
    })
