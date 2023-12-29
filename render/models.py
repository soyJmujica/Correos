from django.db import models

# Create your models here.
class TeamMembers(models.Model):
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	phone = models.CharField(max_length=100, verbose_name="Phone Number")
	email = models.CharField(max_length=100, verbose_name="Email")
	join = models.DateField(verbose_name="Joining Date")
	#picture = models.ImageField(upload_to = 'agent_photos/',blank=True,null = True, verbose_name = "Profile Picture")
	pending = models.IntegerField(default=0)
	closed = models.IntegerField(default=0)

	
	def __str__(self):
		return str(self.first_name + " " + self.last_name)

	'''def save(self, *args, **kwargs):
					self.picture.name = str(self.first_name+"_"+self.last_name+".jpg")
			'''