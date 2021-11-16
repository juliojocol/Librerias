from django.urls import path
from graphene_django.views import GraphQLView
from misitio.schema import schema
from . import views

urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', views.publicacion_lista, name='publicacion_lista'),
    path('articulo/<int:pk>/', views.publicacion_detalle, name='publicacion_detalle'),
    path('articulo/nueva/', views.publicacion_nueva, name='publicacion_nueva'),
    path('publicacion/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),
    path('borradores/', views.publicacion_borrador_lista, name='publicacion_borrador_lista'),
    path('publicacion/<int:pk>/publicar', views.publicacion_publicar, name='publicacion_publicar'),
    path('publicacion/<int:pk>/eliminar', views.publicacion_eliminar, name='publicacion_eliminar'),
    
]