<template>
   

    <center>
        <a :href="`/misitio/crear/`" class="btn btn-outline-success">Crear</a>
        <div class="card text-center" v-for="publicacion in publicaciones " :key="publicacion.id">
            <div class="card-body">
                <h3 class="card-subtitle mb-2 text-muted">{{ publicacion.producto }}</h3>
            </div>
            <div class="card-body">
                <h3 class="card-subtitle mb-2 text-muted">Descripcion</h3> 
                <p class="card-text">{{ publicacion.descripcion }}</p>
            </div>
            <div class="card-body">
                <h3 class="card-subtitle mb-2 text-muted">Precio</h3>
                <p class="card-text">{{ publicacion.precio }}</p>
            </div>
            <div class="card-footer text-muted">
            //<td type="button" class="btn btn-outline-info"><a :href="`/misitio/actualizar`">Actualizar</a></td>
            </div>
        </div>
    </center>



</template>

<script>
    import axios from 'axios'
    export default{
    name: 'Listar',
    data(){
      return {
        publicaciones: []
        }
    },
    async mounted() {
        try {
            var result = await axios({
                method: 'POST',
                url: 'http://localhost:8000/graphql',
                data: {
                    query: `
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