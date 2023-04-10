<template>
  <div class="backdrop">
    <div class="modal">
        <h1> {{ score }} </h1>
        <h1> {{ decision }} </h1>
      </div>
  </div>
</template>

<script>
export default {
    props: ['score', 'decision'],
}
</script>

<style scoped>
.modal {
	width: 24rem;
  color: #33465E;
  background-color: white;
	position: fixed;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
  box-shadow: 0 0 1rem rgba(black, 0.1);
	opacity: 1;
	transition: opacity 550ms ease-in-out;
  border-radius: 10px;
  text-align: center;
}

.backdrop {
  top: 0;
  position: fixed;
  background: rgba(0,0,0,0.5);
  width: 100%;
  height: 100%;
}
</style>