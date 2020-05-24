
from .forms import SignUpForm
from .models import User
from graphene import Field,List, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation


class UserType(DjangoObjectType):
    class Meta:
        model = User

class UserMutation(DjangoModelFormMutation):
    user = Field(UserType)
    class Meta:
        form_class = SignUpForm
        
class Mutation(ObjectType): 
    create_user = UserMutation.Field()

class Query(object):

    users = List(UserType)
    def resolve_users(self,info, **kwargs):
        return User.objects.all()