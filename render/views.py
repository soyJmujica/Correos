from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMembers
from .forms import TeamForm
from Buyer.models import UnderContractBuyer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Count
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

def index(request):
	return render(request,'index.html',{})



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


	return render(request, 'agents.html', {'encabezado':"Team", "agents":agents})


def AgentInfo(request, agent_id):
	agente = get_object_or_404(TeamMembers, pk = agent_id)
	return render(request, 'agentinfo.html',{'encabezado':agente.first_name, 'agent':agente})



def AgentsPending(request, agent_id):
	agente = get_object_or_404(TeamMembers, pk = agent_id)

	properties = UnderContractBuyer.objects.filter(agent = agente, status = "Pending")

	return render(request, 'pendientes.html',{'encabezado':f"Pending Deals Of {agente}",
		"properties":properties})

def AgentsClosed(request,agent_id):
	agente = get_object_or_404(TeamMembers, pk = agent_id)
	properties = UnderContractBuyer.objects.filter(agent = agente, status = "Closed")

	return render(request, 'cerrados.html', {'encabezado': f"Closed Deals Of {agente}",
		'properties':properties})


def AgentsDeals(request, agent_id):
	agente = get_object_or_404(TeamMembers, pk = agent_id)
	properties = UnderContractBuyer.objects.filter(agent=agente)

	return render(request, 'sales.html', {'encabezado':f"All Deals Of {agente}",
		'properties':properties})



