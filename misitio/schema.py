import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from .models import Publicacion

class PublicacionType(DjangoObjectType):
    class Meta:
        model = Publicacion
        fields = ('id', 'producto', 'descripcion', 'precio')

class Query(graphene.ObjectType):
    all_publicacion = graphene.List(PublicacionType)

    def resolve_all_publicacion(root, info):
        return Publicacion.objects.all()


class CrearPublicacion(graphene.Mutation):

    class Arguments:
        producto = graphene.String(required=True)
        descripcion = graphene.String()
        precio = graphene.String()
    
    publicacion = graphene.Field(PublicacionType)

    @classmethod
    def mutate(cls, root, info, producto, descripcion, precio):
        publicacion = Publicacion(
            producto=producto,
            descripcion=descripcion,
            precio=precio
        )
        publicacion.save()
        return CrearPublicacion(publicacion=publicacion)

class ActualizarPublicacion(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        producto = graphene.String(required=True)
        descripcion = graphene.String()
        precio = graphene.String()

    publicacion = graphene.Field(PublicacionType)

    @classmethod
    def mutate(cls, root, info, producto, descripcion, precio, id):
        publicacion = Publicacion.objects.get(id=id)
        publicacion.producto = producto
        publicacion.descripcion = descripcion
        publicacion.precio = precio
        publicacion.save()
        return ActualizarPublicacion(publicacion=publicacion)

class EliminarPublicacion(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    publicacion = graphene.Field(PublicacionType)

    @classmethod
    def mutate(cls, root, info, id):
        publicacion = Publicacion.objects.get(id=id)
        publicacion.delete()
        return ActualizarPublicacion(publicacion=publicacion)


class Mutation(graphene.ObjectType):

    crear_publicacion = CrearPublicacion.Field()
    actualizar_publicacion = ActualizarPublicacion.Field()
    eliminar_publicacion = EliminarPublicacion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)