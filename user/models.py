import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import random 
from django.forms import model_to_dict
from crum import get_current_request

class User(AbstractUser):
    dni = models.CharField('Documento', max_length=50, unique = True)
    phone_user = models.CharField('Telefono', max_length=50)
    observacion = models.CharField(verbose_name='Observacion', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def toJSON(self):
        item = model_to_dict(self, exclude=['password','user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item
    
    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

    def _str_(self):
        return f'{self.first_name} {self.last_name}'
