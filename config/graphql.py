import graphene

from shorten.graphql.queries import UrlQuery
# from src.shorten.graphql.mutations import UrlMutation

class Query(UrlQuery,#):
            graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


# schema: graphene.Schema = graphene.Schema(query=Query, mutation=Mutation)
schema: graphene.Schema = graphene.Schema(query=Query)
