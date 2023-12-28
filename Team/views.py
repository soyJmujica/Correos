from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMembers
from .forms import TeamForm
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

