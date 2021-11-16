<template>

  <center>
    <div>
    <h1>Agregar un nuevo articulo</h1>
    <br>
    <form  action="" @submit.prevent="mounted()">
      <div class="card-body">
         <div class="card-subtitle mb-2 text-muted">
        <h3>Producto</h3>
        <input v-model="producto" producto="" type="text" class="form-control">
        <h3>Descripcion</h3>
        <input v-model="descripcion" descripcion="" type="text" class="form-control">
        <h3>Precio</h3>
        <input v-model="precio" precio="" type="text" class="form-control">
        <br>
        <button type="submit" class="btn btn-outline-info" name="button">Crear</button>
        </div>
      </div>
    </form>
  </div>
  </center>

</template>

<script>
  import axios from 'axios'
  export default{
    name: 'publicaciones',
    data(){
      return {
        producto: '',
        descripcion: '',
        precio: '',
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
  crearpublicacion(Producto:"`+this.producto+`",descripcion:"`+this.descripcion+`",precio:"`+this.precio+`"){
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