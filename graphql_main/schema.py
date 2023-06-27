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
    
    
class CreateCategory(graphene.Mutation):
    class Arguments:
        new_name = graphene.String(required=True)
        
    category = graphene.Field(CategoryModelType)

    def mutate(self, info, new_name):
            category = Category.objects.create(name=new_name)
            return CreateCategory(category=category)
        
    
class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        update_name = graphene.String()
        
    category = graphene.Field(CategoryModelType)
    
    def mutate(self, info, id, update_name):
        category = Category.objects.get(id=id)
        if update_name:
            category.name = update_name
        category.save()
        return UpdateCategory(category=category)
            
            
class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteCategory(success=True)
    

class CreatePost(graphene.Mutation):
    class Arguments:
        new_image = graphene.String(required=True)
        new_title = graphene.String(required=True)
        new_description = graphene.String(required=True)
        new_category = graphene.Int(required=True)
        new_location = graphene.String(required=True)
        
        
    post = graphene.Field(PostModelType)

    def mutate(self, info, new_image, new_title, 
               new_description, new_category, new_location):
        post = Post.objects.create(image=new_image, 
                                   title=new_title, 
                                   description=new_description, 
                                   category=Category.objects.get(id=new_category), 
                                   location=new_location)
        return CreatePost(post=post)
        
    
class UpdatePost(graphene.Mutation):
    class Arguments:
        new_id = graphene.ID(required=True)
        new_image = graphene.String(required=True)
        new_title = graphene.String(required=True)
        new_description = graphene.String(required=True)
        new_category = graphene.Int(required=True)
        new_location = graphene.String(required=True)
        
    post = graphene.Field(PostModelType)
    
    def mutate(self, info, new_id, new_image, new_title, 
               new_description, new_category, new_location):
        post = Post.objects.get(id=new_id)
        if new_image:
            post.image = new_image
        if new_title:
            post.title = new_title
        if new_description:
            post.description = new_description
        if new_category:
            post.category = Category.objects.get(id=new_category)
        if new_location:
            post.location = new_location
        post.save()
        return UpdatePost(post=post)
            
            
class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        post = Post.objects.get(id=id)
        post.delete()
        return DeletePost(success=True)
    
            
class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)
    
    
