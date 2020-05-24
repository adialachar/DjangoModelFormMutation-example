import graphene
import survey.schema

class Mutation(survey.schema.Mutation,graphene.ObjectType):
    pass

class Query(survey.schema.Query,graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)