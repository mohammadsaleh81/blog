
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from account.forms import ProfileForm
from account.mixins import FieldsMixin, FormvalidMixin, AuthorAccessMixin, SuperUserAccessMixin
from account.models import User
from blog.models import Article

# Create your views here.

class ArticleList(LoginRequiredMixin, ListView):
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)
	template_name = "registration/home.html"



class ArticleCreate(LoginRequiredMixin,FieldsMixin,FormvalidMixin ,CreateView):
	model = Article
	template_name = 'registration/article_create_update.html'


class ArticleUpdate( FieldsMixin, FormvalidMixin,AuthorAccessMixin, UpdateView):
	model = Article
	template_name = 'registration/article_create_update.html'

class ArticleDelete(SuperUserAccessMixin,DeleteView):
	model = Article
	template_name = 'registration/article_confirm_delete.html'
	success_url = reverse_lazy('account:home')

class Profile(LoginRequiredMixin,UpdateView):
	model = User
	template_name = 'registration/profile.html'
	success_url = reverse_lazy('account:profile')
	form_class = ProfileForm

	def get_object(self):
		return User.objects.get(pk= self.request.user.pk)


	def get_form_kwargs(self):
		kwargs = super(Profile, self).get_form_kwargs()
		kwargs.update({
			'user': self.request.user
		})
		return kwargs