import graphene

from shorten.graphql.queries import UrlQuery
from shorten.graphql.mutations import UrlMutations

class Query(UrlQuery,
            graphene.ObjectType):
    pass


class Mutation(UrlMutations,
               graphene.ObjectType):
    pass


schema: graphene.Schema = graphene.Schema(query=Query, mutation=Mutation)
