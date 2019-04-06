from graphene_django import DjangoObjectType
import graphene

from qna_app import models

class Organization(DjangoObjectType):
    class Meta:
        model = models.Organization

class Query(graphene.ObjectType):
    organizations = graphene.List(Organization)

    def resolve_organizations(self, info):
        return models.Organization.objects.all()

schema = graphene.Schema(query=Query)