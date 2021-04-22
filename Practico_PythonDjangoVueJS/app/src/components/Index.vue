<template>
    <div class="pt-5">
        <div v-if="subcripciones && subcripciones.length">
            <div class="card mb-3" v-for="subcripcion of subcripciones" v-bind:key="subcripcion.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <svg class="bd-placeholder-img" width=200 xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>{{ subcripcion.nombre }}</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ subcripcion.nombre.charAt(0) }}</text></svg>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">{{subcripcion.nombre}}</h5>
                            <p class="card-text">{{subcripcion.descripcion}}</p>
                            <router-link :to="{name: 'edit', params: {id: subcripcion.id}}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="eliminarSubcripcion(subcripcion)">Eleminar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p v-if="subcripciones.length == 0">No hay subcripciones</p>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    data() {
        return {
            subcripciones: []
        }
    },
    created(){
        this.all();
    },
    methods: {
        eliminarSubcripcion: function(subscr) {
            if (confirm('Eliminar ' + subscr.nombre)){
                axios.delete('http://localhost:8000/api/subcripciones/${subscr.id}')
                .then(response => {
                        this.all();
                    });
            }
        },
        all: function() {
            axios.get('http://localhost:8000/api/subcripciones')
            .then(response => {
                this.subcripciones = response.data
            });
        },
    }
}

</script>