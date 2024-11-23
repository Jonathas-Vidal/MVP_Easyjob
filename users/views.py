from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserProfileForm

class UserCreateView(CreateView):
    model = Users
    form_class = UserProfileForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        try:
            # Salva o usuário criado
            form.save()
            messages.success(self.request, 'Cadastro realizado com sucesso!')
            return super().form_valid(form)
        except Exception as e:
            # Se houver um erro ao salvar, exibe a mensagem de erro
            messages.error(self.request, f'Erro ao cadastrar: {str(e)}')
            return self.form_invalid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('home')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def home_view(request):
    return render(request, 'home.html')

@method_decorator(login_required, name='dispatch')
class UserProfileView(DetailView):
    model = Users
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return self.request.user.users 

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = Users
    form_class = UserProfileForm
    template_name = 'users/edit_profile.html'
    context_object_name = 'form'

    # Redireciona o usuário para o perfil após a edição
    def get_success_url(self):
        return reverse_lazy('profile')  # Redireciona para a página de perfil após salvar

    # Usa o usuário autenticado para pegar os dados do perfil
    def get_object(self, queryset=None):
        return self.request.user.users  # Acessa o perfil do usuário autenticado

    # Personaliza o contexto (opcional)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Seu perfil foi atualizado com sucesso.')
        return super().form_valid(form)


@login_required
def delete_profile(request):
    if request.method == 'POST':
        # Lógica para excluir o perfil
        user = request.user
        user.delete()  # Exclui o usuário
        messages.success(request, "Perfil excluído com sucesso!")
        return redirect('home')  # Redireciona para a página inicial após a exclusão
    return render(request, 'users/delete_profile.html')