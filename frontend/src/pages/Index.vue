<template>
  <q-page class="flex flex-center">
    <h4>{{ currentTime }}</h4>
  </q-page>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PageIndex',
  data () {
    return {
      currentTime: null
    }
  },
  mounted () {
    axios.get('/api/time')
      .then((resp) => {
        this.currentTime = resp.data.time
      })
      .catch((err) => {
        this.currentTime = err
      })
  }
}
</script>
