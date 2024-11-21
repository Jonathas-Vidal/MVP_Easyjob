from .models import Service
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ServiceForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Users

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.order_by('-idServico')

@method_decorator(login_required, name='dispatch')
class MyServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(idPrestador=self.request.user).order_by('-idServico')

class ServiceSearchView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            services = Service.objects.filter(titulo__icontains=query)
            if not services.exists():
                messages.error(self.request, 'Nenhum serviço encontrado.')
            return services
        return Service.objects.all()

    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

    def get_object(self):
        return Service.objects.get(pk=self.kwargs['pk'])



@method_decorator(login_required, name='dispatch')
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = reverse_lazy('service-list')

    def dispatch(self, request, *args, **kwargs):
        # Verifica se o usuário tem a função 'Prestador'
        if request.user.funcao != 'P':
            messages.error(request, "Você precisa ser um Prestador para criar serviços.")
            return redirect('home')  # Redireciona para a home se não for prestador
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.idPrestador = self.request.user  # Atribui o prestador ao serviço
        messages.success(self.request, 'O serviço foi criado com sucesso')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

@method_decorator(login_required, name='dispatch')
class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    context_object_name = 'form'
    
    def get_success_url(self):
        return reverse_lazy('service-detail', args=[self.object.pk])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'O serviço foi atualizado com sucesso')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_delete.html'
    context_object_name = 'service'
    success_url = reverse_lazy('service-list')

    def get_success_url(self):
        messages.error(self.request, 'O serviço foi deletado com sucesso')
        return super().get_success_url()

