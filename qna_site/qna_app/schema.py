from graphene_django import DjangoObjectType
import graphene

from qna_app import models


class Organization(DjangoObjectType):
    class Meta:
        model = models.Organization


class Role(DjangoObjectType):
    class Meta:
        model = models.Role


class Staff(DjangoObjectType):
    class Meta:
        model = models.Staff


class Question(DjangoObjectType):
    class Meta:
        model = models.Question


class Query(graphene.ObjectType):
    organizations = graphene.List(Organization)
    staff = graphene.List(Staff)
    roles = graphene.List(Role)
    questions = graphene.List(Question)

    def resolve_organizations(self, info):
        return models.Organization.objects.all()

    def resolve_staff(self, info):
        return models.Staff.objects.all()

    def resolve_roles(self, info):
        return models.Role.objects.all()

    def resolve_questions(self, info):
        return models.Question.objects.all()


schema = graphene.Schema(query=Query)
