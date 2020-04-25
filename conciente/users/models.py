from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Nombre"), blank=True, max_length=255)
    last_name = CharField(("Apellido"), max_length=255)
    phone = CharField(("Phone of User"), blank=True, max_length=10)
    cedula = CharField(("Cedula"), max_length=255)
    photo = ImageField(upload_to="imagenes_usuarios")
    bio = CharField(("Biografia"), max_length=600)
    speciality = CharField(("Especialidad"), blank=True, max_length=100)
    social_network = CharField(("Especialidad"), blank=True, max_length=255)



    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
