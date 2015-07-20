from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from mindframe.models import Topic, TopicEntry, UserProfile, UserToGroup
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	user=request.user
	userToGroup = UserToGroup.objects.all()
	topics = Topic.objects.all()
	topicList = list()

	for i in userToGroup:
		for topic in topics:
			if i.user == user and i.group == topic.group:
				topicList.append(topic)
			else:
			    pass	
	pics = UserProfile.objects.all()
	context = {'topics':topicList, 'pics':pics}
	return render(request, 'index.html',context)

@login_required	
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    entries = TopicEntry.objects.all()
    entryList = list()

    for i in entries:
    	if i.topic.id == topic.id:
    		entryList.append(i)
    	else:
    		pass

    context = {'topic':topic,'entries': entryList, 'next':request.path}
    return render(request, 'topic.html', context)

@login_required
def createTopic(request):
	return render(request, 'createTopic.html')

@login_required
def createEntry(request):
	return render(request, 'createEntry.html')

@login_required
def createGroup(request):
	return render(request, 'createGroup.html')	

@login_required
def users(request):
	users=User.objects.all()
	context={'users':users}
	return render(request,'users_template.html')

@login_required
def entries(requesti,topicID):
	topicEnts = TopicEntry.objects.all()
	return HttpResponse(topicEnts)

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
		return HttpResponseRedirect('/index')
	else:
		return HttpResponseRedirect('/invalid')

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
	
	return render_to_response('createUser.html', args)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login')