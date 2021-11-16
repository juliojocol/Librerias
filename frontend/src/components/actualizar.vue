<template>
     <center>
    <div>
    <h1>Actualizar Producto</h1>
    <br>
    <h2>Id de producto: {{id=$route.params.id}} </h2>
    <form  action="" @submit.prevent="mounted()">
      <div class="card-body">
         <div class="card-subtitle mb-2 text-muted">
        <h3>Producto</h3>
        <input v-model="producto" type="text" class="form-control">
        <h3>Descripcion</h3>
        <input v-model="descripcion" type="text" class="form-control">
        <h3>Precio</h3>
        <input v-model="precio" type="text" class="form-control">
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
    name: 'Publicaciones',
    data(){
      return {
        producto: this.$route.params.producto,
        descripcion: this.$route.params.descripcion,
        precio: this.$route.params.precio,
        id: '',
        directory: []
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
  actualizarPublicacion(input:{id:"`+this.id+`", producto:"`+this.producto+`", descripcion:"`+this.descripcion+`",precio:"`+this.precio+`"}){
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
        this.directory = result.data.data.allPublicacion
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>