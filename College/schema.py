import graphene
from graphene_django import DjangoObjectType #used to change Django object into a format that is readable by GraphQL
from Student.models import CompoundV,StudentContact

class CompoundVType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = CompoundV
        field = ("__all__")
        """id", "name", "borrowRate","cash",'collateralFactor',"exchangeRate","interestRateModelAddress","reserves","supplyRate","symbol","totalBorrows","totalSupply","underlyingAddress","underlyingName","underlyingPrice","underlyingSymbol","reserveFactor","underlyingPriceUSD")"""

class Query(graphene.ObjectType):
    #query ContactType to get list of contacts
    list_compound=graphene.List(CompoundVType)

    def resolve_list_compound(root, info):
        # We can easily optimize query count in the resolve method
        return CompoundV.objects.all()
class ContactType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = StudentContact
        field = ("__all__")
        """id", "name", "borrowRate","cash",'collateralFactor',"exchangeRate","interestRateModelAddress","reserves","supplyRate","symbol","totalBorrows","totalSupply","underlyingAddress","underlyingName","underlyingPrice","underlyingSymbol","reserveFactor","underlyingPriceUSD")"""

class Query2(graphene.ObjectType):
    #query ContactType to get list of contacts
    list_contact=graphene.List(ContactType)
    list_compound=graphene.List(CompoundVType)
    def resolve_list_contact(root, info):
        # We can easily optimize query count in the resolve method
        return StudentContact.objects.all()
    def resolve_list_compound(root, info):
        # We can easily optimize query count in the resolve method
        return CompoundV.objects.all()
schema = graphene.Schema(query=(Query2))