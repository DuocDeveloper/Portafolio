<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="name">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="subscription.name"
                    v-validate="'required'"
                    name="name"
                    placeholder="Ingrese el nombre"
                    :class="{'is-invalid': errors.has('subcripcion.nombre') && submitted}">
                <div class="invalid-feedback">
                    Favor debe ingresar un nombre
                </div>
            </div>
            <div class="form-group">
                <label for="moneda">Moneda</label>
                <select
                    name="moneda"
                    class="form-control"
                    v-validate="'required'"
                    id="moneda"
                    v-model="subcripcion.moneda"
                    :class="{'is-invalid': errors.has('subcripcion.moneda') && submitted}">
                    <option value="EUR">EUR</option>
                    <option value="USD">USD</option>
                    <option value="CLP">CLP</option>
                </select>
                <div class="invalid-feedback">
                    Favor debe ingresar una moneda.
                </div>
            </div>
            <div class="form-group">
                <label for="monto">Monto</label>
                <input
                    type="number"
                    name="monto"
                    v-validate="'required'"
                    class="form-control"
                    id="amount"
                    v-model="subcripcion.monto"
                    placeholder="Ingrese el monto"
                    :class="{'is-invalid': errors.has('subcripcion.monto') && submitted}">
                <div class="invalid-feedback">
                    Favor debe ingresar un monto
                </div>
            </div>
            <div class="form-group">
                <label for="descripcion">Descripcion</label>
                <textarea
                    name="descripcion"
                    class="form-control"
                    id="descripcion"
                    v-validate="'required'"
                    v-model="subcripcion.descripcion"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('subcripcion.descripcion') && submitted}"></textarea>
                <div class="invalid-feedback">
                    Favor debe ingresar una descripción
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Enviar</button>
        </form>
    </div>
</template>

<script>
import axios from "axios";

export default{
    data() {
        return {
            subcripcion: {
                nombre: '',
                moneda: '',
                monto: '',
                descripcion: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function(e){
            this.$validator.validate().then(result => {
                this.submitted = true;
                if(!result){
                    return;
                }
                console.log(this.moneda)
                axios.post('http://localhost:8000/api/subcripciones/', this.subcripcion)
                .then(response => {
                    this.$router.push('/');
                })
            });
        }
    },
}
</script>