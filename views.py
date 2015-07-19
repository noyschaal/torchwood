from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from mindframe.models import Topic, TopicEntry, UserProfile
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
	topics = Topic.objects.all()
	pics = UserProfile.objects.all()
	context = {'topics':topics, 'pics':pics}
	return render(request, 'index.html',context) 
	

@login_required	
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    context = {'topic':topic, 'next':request.path}
    return render(request, 'topic.html', context)

def createTopic(request):
	return render(request, 'createTopic.html')
	
def createGroup(request):
	return render(request, 'createGroup.html')	

def users(request):
	users=User.objects.all()
	context={'users':users}
	return render(request,'users_template.html')

def entries(requesti,topicID):
	topicEnts = TopicEntry.objects.all()
	return HttpResponse(topicEnts)

def spetopic(request):	
	context = {'next':request.path}
	return render(request, 'topic_template.html',context)

#user authintication views

def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html', c)
	
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')
		
def loggedin(request):
	return render_to_response('loggedin.html',
								{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	print args
	return render_to_response('createUser.html', args)