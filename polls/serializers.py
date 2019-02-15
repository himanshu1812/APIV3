from rest_framework.serializers import ModelSerializer,CharField,EmailField
from .models import *
from django.db.models import Q
from django.forms import ValidationError

class UserCreateSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = [
        'name',
        'house_name',
        'email',
        'password',
    ] 

class RoomCreateSerializer(ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__' 

class UserLoginSerializers(ModelSerializer):
  token = CharField(allow_blank = True, read_only=True)
  email =   EmailField(label = "Email Address")

  class Meta:
    model = User
    fields = ['token','email','password']
    extra_kwargs = {"password":{"write_only":True}}
  def validate(self,data):
    user_obj = None
    email = data.get("email",None)
    password = data["password"]

    if not email:
      raise ValidationError("A Email is Required To login")

    user = User.objects.filter(
            Q(email=email)
    ).distinct() 
    if user.exists() and user.count() == 1:
      user_obj = user.first()
    else:
      raise ValidationError("This Email is Not Valid")

    if user_obj:
      if not user_obj.check_password(password):
        raise ValidationError("Incorrect Password")
    data["token"] = "Some Random Token"
    return data
