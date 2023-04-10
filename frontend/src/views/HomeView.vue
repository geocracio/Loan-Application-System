<template>
  <main>
    <InputForm @backendResponse="handleBackendResponse" />
    <div v-if="showModal"> 
      <ModalResults :score="score" :decision="decision" />
    </div>
  </main>
</template>

<script>
import InputForm from '../components/InputForm.vue'
import ModalResults from '../components/ModalResults.vue'

export default {
  components: {
    InputForm, 
    ModalResults
  },
  data() {
    return{
      score: null,
      decision: null,
      showModal: false,
      backendResponse: null
    } 
  },
  methods:{
    handleBackendResponse(data){
      this.backendResponse = data
      this.score = data.probability
      this.decision = data.prediction
      this.showModal = true
    }
  }
}
</script>

<style>
</style>
