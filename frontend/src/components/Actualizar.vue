<template>
  <center>
    <div>
    <h1>Actualizar un articulo</h1>
    <br>
    <form action="" @submit.prevent="mounted()">
      <div class="card-body">
         <div class="card-subtitle mb-2 text-muted">
         <h3>Id producto</h3>
         <input v-model="id" id="" type="text" class="form-control">
        <h3>Producto</h3>
        <input v-model="producto" producto="" type="text" class="form-control">
        <h3>Descripcion</h3>
        <input v-model="descripcion" descripcion="" type="text" class="form-control">
        <h3>Precio</h3>
        <input v-model="precio" precio="" type="text" class="form-control">
        <br>
    <button type="submit" class="btn btn-outline-info" name="button">Actualizar</button>
    </div>
    </div>
    </form>
  </div>
  </center>
</template>

<script>
  import axios from 'axios'
  export default{
    name: 'Actualizar',
    data(){
      return {
        producto: this.$route.params.producto,
        descripcion: this.$route.params.descripcion,
        precio: this.$route.params.precio,
        id: '',
        publicaciones: []
      }
    },
    methods: {
    async mounted () {
  try {
        var result = await axios({
          method: 'POST',
          url: 'http://localhost:8000/graphql',
          data: {
            query: `
            mutation{
              actualizarPublicacion(id:"`+this.id+`", producto:"`+this.producto+`", descripcion:"`+this.descripcion+`",precio:"`+this.precio+`"){
                publicacion{
                  id
                  producto
                  descripcion
                  precio
                }
              }
            } 
            `
          } 
        })
        this.publicaciones = result.data.data.actualizarPublicacion
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>