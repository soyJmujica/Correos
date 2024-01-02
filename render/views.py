from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMembers
from .forms import TeamForm
from Buyer.models import UnderContractBuyer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def AddAgent(request):
	if request.method == 'POST':
		form = TeamForm(request.POST, request.FILES)
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
	agents = TeamMembers.objects.all()
	closed = UnderContractBuyer.objects.values('agent','status').annotate(Count('agent'))
	a = closed.values_list('agent','status','agent__count')
	for agent in agents:
		for count in a:
			if agent.id == count[0]:
				if count[1]=='Pending':
					agent.pending = count[2]
				elif count[1]=='Closed':
					agent.closed = count[2]
		agent.save()


	return render(request, 'agents.html', {'encabezado':"Team", "agents":agents})



'''
def Agents(request):
	agents = TeamMembers.objects.all()
	closed = UnderContractBuyer.objects.values('agent','status').annotate(Count('agent'))
	a = closed.values_list('agent','status','agent__count')
	for agent in agents:
		for count in a:
			if agent.id == count[0]:
				if count[1]=='Pending':
					agent.pending = count[2]
				elif count[1]=='Closed':
					agent.closed = count[2]
		agent.save()


	return render(request, 'agents.html', {'encabezado':"Team", "agents":agents})'''



def AgentsPending(request, agent_id):
	properties = UnderContractBuyer.objects.filter(agent = agent_id, status = "Pending")

	return render(request, 'pendientes.html',{'encabezado':f"Pending Deals Of {properties.agent_id}",
		"properties":properties})



