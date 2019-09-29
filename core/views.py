from django.shortcuts import render
# from django.views.generic import TemplateView
from .models import About, Service, RecentWork, Contact
from django.core.mail import send_mail
from django.conf import settings
# from .forms import ContactForm
from .models import Contact
# Create your views here.
# class HomeTemplateView(TemplateView):
# 	template_name='home.html'
# 	#override get context data method
# 	def get_context_data(self, **kwargs):
# 		context=super().get_context_data(**kwargs) #girst get super get context data
# 		context['about']=About.objects.first()
# 		context['services']=Service.objects.all()
# 		context['works']=RecentWork.objects.all()
# 		return context

def home(request):
	context={
	'about':About.objects.first(),
	'services':Service.objects.all(),
	'works':RecentWork.objects.all(),
	}
	if request.method =='POST':
		print(request.POST)
		name=request.POST.get('name')
		email_from=request.POST.get('email_from')
		email_to=request.POST.get('email_to')
		message=request.POST.get('message')
		subject = 'Welcome to my site'
		recipient_list = [email_to,]
		contact=Contact(name=name, email=email_from, to=email_to,  message=message)
		contact.save()
		send_mail( subject, message, email_from, recipient_list, fail_silently=False)
		return render(request,'home.html', context)

	return render(request,'home.html', context)