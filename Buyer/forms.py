from django.forms import ModelForm
from django import forms
from .models import UnderContractBuyer


class BuyerForm(ModelForm):
	"""docstring for BuyerForm"""
	class Meta:
		model = UnderContractBuyer
		fields = ['team','agent','address','buyer_firstname','buyer_lastname','buyer_email', 'buyer_phone',
		'efective','closing', 'escrow_time','inspection_time','loan_time',
		'titlecompany','titleagent','titlecompany_address','titlecompany_email', 'titlecompany_phone',
		#'screenshot', 
		'other_agent','other_agent_phone','other_agent_email','other_agent_company',
		'price','escrow_amount', 'mls_fee','commission',
		'inspectionteam','inspectionteam_email','inspectionteam_phone', "insurance",
		"financing",'lender','lender_phone','lender_email',
		"thereis_HOA","HOA","HOA_phone", "HOA_email"]
		






