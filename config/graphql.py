import graphene

from shorten.graphql.queries import UrlQuery
from shorten.graphql.mutations import UrlMutations

class Query(UrlQuery, graphene.ObjectType):
    '''All project queries.'''
    pass


class Mutation(UrlMutations, graphene.ObjectType):
    '''All project mutations.'''
    pass


schema: graphene.Schema = graphene.Schema(query=Query, mutation=Mutation)
