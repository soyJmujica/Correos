from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UnderContractBuyer
from .forms import BuyerForm
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import smtplib

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


def details(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)
	
	return render(request, 'detalles.html', {'property': address,
		'encabezado':address.address})

def emails(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk=property_id)
	return render(request, '7correos.html',{'encabezado':address.address, 'property':address})


def saleclosed(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)
	address.status = "Closed"
	address.save()

	return render(request, 'detalles.html', {'property': address,
		'encabezado':address.address})

def closed(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)

	return render(request, 'cerrado.html', {'encabezado':address.address,
		'property':address})
def salepending(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk=property_id)
	address.status = "Pending"
	address.save()

	return render(request, 'detalles.html', {'property': address,
		'encabezado':address.address})


def congratulations_send(mail):
	template = render_to_string('congratulations.html',{'property':mail})
	content = template
		
	email = EmailMultiAlternatives(
					subject = f"Congratulations!! We are under contract on {mail.address}",
					body = '',
					from_email = settings.EMAIL_HOST_USER,
					to = [mail.buyer_email],
					cc = []
			
					)
	email.attach_alternative(content, 'text/html')

	email.send()


def TCemail_send(mail):
	template = render_to_string('TCemail.html', {'property':mail})
	content = template

	email = EmailMultiAlternatives(
		subject=f"Information about {mail.address}",
		body='',
		from_email=settings.EMAIL_HOST_USER,
		to = [mail.titlecompany_email],
		cc = []

		)
	email.attach_alternative(content, 'text/html')

	email.send()

def Lender_send(mail):
	template = render_to_string('Lender email.html', {'property':mail})
	content = template

	email = EmailMultiAlternatives(
		subject=f"Information for {mail.lender} about {mail.address}",
		body='',
		from_email=settings.EMAIL_HOST_USER,
		to = [mail.lender_email],
		cc = []
		)
	email.attach_alternative(content, 'text/html')

	email.send()

def Title_send(mail):
	template = render_to_string('Title email buyer.html', {'property':mail})
	content = template

	email = EmailMultiAlternatives(
		subject = f"Important Information about {mail.address}",
		body='',
		from_email=settings.EMAIL_HOST_USER,
		to = [mail.titlecompany_email],
		cc = []
		)
	email.attach_alternative(content,'text/html')

	email.send()


def emailsend(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)

	if request.method == 'GET':
		mail = address
		print("Enviando correo")
		congratulations_send(mail)
		print('Congratulations enviado')
		TCemail_send(mail)
		print('TCemail enviado')
		Lender_send(mail)
		print("Lender's Email send")
		Title_send(mail)
		print('Title email send')

	return render(request, 'detalles.html', {'encabezado':address.address,
		'property':address})

