import graphene 
from graphene_django import DjangoObjectType
from main.models import Category, Post


class CategoryModelType(DjangoObjectType):
    class Meta:
        model = Category
        
        
class PostModelType(DjangoObjectType):
    class Meta:
        model = Post
        
        
class Query(graphene.ObjectType):
    category_model = graphene.List(CategoryModelType)
    post_model = graphene.List(PostModelType)
    
    def resolve_category_model(self, info):
        return Category.objects.all()
    
    def resolve_post_model(self, info):
        return Post.objects.all()
    

schema = graphene.Schema(query=Query)
    
    
