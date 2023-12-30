from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UnderContractBuyer
from .forms import BuyerForm

# Create your views here.

def undercontract(request):
	if request.method == 'POST':
		form = BuyerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('transacciones')
	else:
		form = BuyerForm()
	return render(request, "undercontract.html", {'form':form,
		'encabezado':"Under Contract Buyer"})


def transactions(request):
	filtro = request.GET.get('filtro',)
	if filtro == 'Enviado':
		properties = UnderContractBuyer.objects.filter(emailsend = True)
	elif filtro == 'No Enviado':
		properties = UnderContractBuyer.objects.filter(emailsend = False)
	else:
		properties = UnderContractBuyer.objects.all()
	return render(request, 'transacciones.html',{'encabezado':'Transactions','properties':properties})
