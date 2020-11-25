<template>
  <div class="home">
    <v-data-table
      :headers="headers"
      :items="desserts"
      item-key="name"
      class="elevation-1"
      :search="search"
      :custom-filter="filterOnlyCapsText"
    >
      <template v-slot:top>
        <v-text-field
          v-model="search"
          label="Search (UPPER CASE ONLY)"
          class="mx-4"
        ></v-text-field>
      </template>
     
    </v-data-table>
  </div>
</template>

<script>


export default {
  name: 'Home',
  computed:{
    headers(){
      return[
        {text:'Name',value:'name'},
        {text:'Brand', value:'brand'},
        {text:'Type', value:'item_type'},
        {text:'Desire', value:'desire'},
        {text:'Sales', value:'sales'},
        {text:'Expire', value:'expire_date'}
      ]
    }

  }

}
</script>
