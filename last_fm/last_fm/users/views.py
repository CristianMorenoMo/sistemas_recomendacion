from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView,TemplateView,ListView,CreateView,FormView
from django.contrib.auth.views import LoginView , LogoutView


from last_fm.items.models import Items,Artist,Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render
from users.forms import SignupForm
User = get_user_model()


class Index(ListView):
	template_name = 'index.html'
	model = Items
	paginate_by = 20

	def get_queryset(self):
		query=None
		if('name_search' in self.request.GET) and self.request.GET['name_search'] != "":
			query = Q(name_item =self.request.GET['name_search'])

		if query is not None:
			items = Items.objects.filter(query)
		else:
			items = Items.objects.all()
		return items
	
class Browse(ListView):
	template_name = 'browse.html'
	model = Items
	paginate_by = 20

	def get_queryset(self):
		query=None
		if('name_search' in self.request.GET) and self.request.GET['name_search'] != "":
			query = Q(name_item =self.request.GET['name_search'])

		if query is not None:
			items = Items.objects.filter(query)
		else:
			items = Items.objects.all()
		return items


class SingOut(LogoutView):
	next_page = reverse_lazy('index')

class SingIn(LoginView):
	template_name = 'login.html'
	def get(self, request,*arg,**kwargs):
		if request.user.is_authenticated:
		   return HttpResponseRedirect(reverse('index'))
		else:
			context = self.get_context_data(**kwargs)
			return self.render_to_response(context)
	def get_success_url(self):
		return reverse('index')


class SignUpView(FormView):
    """Users sign up view."""
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        """Save form data """
        form.save()
        return super().form_valid(form)





