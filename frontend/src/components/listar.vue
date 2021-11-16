<template>
    <center>
    
        <a :href="`/misitio/crear/`" class="btn btn-outline-success">Crear</a>
        <div class="card text-center" v-for="listar in publicaciones.edges" :key="listar.id">
            <div class="card-body">
                <h3 class="card-subtitle mb-2 text-muted">{{ listar.producto }}</h3>
            </div>
            <div class="card-body">
                <h3 class="card-subtitle mb-2 text-muted">Descripcion</h3> 
                <p class="card-text">{{ listar.descripcion }}</p>
            </div>
            <div class="card-body">
                <h3 class="card-subtitle mb-2 text-muted">Precio</h3>
                <p class="card-text">{{ listar.precio }}</p>
            </div>
            <div class="card-footer text-muted">
            //<td type="button" class="btn btn-outline-info"><a :href="`/misitio/actualizar/${listar.id}/${listar.producto}/${listar.descripcion}/${listar.precio}`">Actualizar</a></td>
            </div>
        </div>
    </center>
</template>

<script>
    import axios from 'axios'
    import gql from 'graphql-tag'
    export default{
    name: 'Publicaciones',
    data(){
      return {
        publicaciones: []
        }
    },
    async mounted () {
    try {
    var result = await axios({
    method: 'POST',
    url: 'http://localhost:8000/graphql',
    data: {
      query: gql`query {
      {
          allPublicacion {
                        id,
                        producto,
                        descripcion,
                        precio
                }
      }
      `
    }
    })
    this.publicaciones = result.data.data.allPublicacion
    } catch (error) {
    console.error(error)
    }
    }
  }
</script>