from django.shortcuts import redirect, render

def login_view(request):
    if request.method == 'POST':
        # Lógica de autenticação
        return redirect('questionario')
    return render(request, 'app_egressos/login.html')

def questionario_view(request):
    return render(request, 'app_egressos/questionario.html')