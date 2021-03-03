import csv
import io
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
#######

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView,TemplateView,ListView,CreateView,FormView
from django.contrib.auth.views import LoginView , LogoutView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
##########
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from last_fm.items.models import Items,Profile

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
from django.shortcuts import render
from users.forms import SignupForm
User = get_user_model()


class Index(ListView):
	template_name = 'index.html'
	model = Items
	paginate_by = 20


	
class Browse(ListView):
	template_name = 'index.html'
	model = Items
	paginate_by = 20
	
	@csrf_exempt
	def post(self, request):
         if('search' in request.POST) and self.request.POST['search'] != "":
            query = Q(name_item = request.POST["search"])

         if query is not None:
            items = Items.objects.filter(query)
         else:
            items = Items.objects.all()
         return items


class SingOut(LogoutView):
	next_page = reverse_lazy()

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





@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def profile_upload(request):
    # declaring template
    template_name = "upload.html"
    data = Items.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address, phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')


    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Items.objects.update_or_create(
            id_item = column[0],
            name_item = column[1],
            name_art = column[2],
        )
    context = {}
    return render(request, template_name, context)





