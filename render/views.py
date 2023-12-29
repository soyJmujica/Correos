from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMembers
from .forms import TeamForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def AddAgent(request):
	if request.method == 'POST':
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('agentes')
	else:
		form = TeamForm()
	return render(request, 'addagent.html', {'encabezado':'Add New Agent To The Team',
		'form':form})

def Agents(request):
	agentes=TeamMembers.objects.all()
	return render(request, 'agents.html', {'encabezado':"Team", 'agents':agentes})

def index(request):
	return render(request,'index.html',{})

def AgentInfo(request, agent_id):
	agente = get_object_or_404(TeamMembers, pk = agent_id)
	return render(request, 'agentinfo.html',{'encabezado':agente.first_name, 'agent':agente})



