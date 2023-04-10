<template>
  <div class="modal">
  <article class="modal__article">
    <h4 class="modal-title"></h4>
    <p class="modal-msg"></p>
  </article>
  
  <footer>
    <button class="button -full -close">close</button>
  </footer>
</div>
</template>

<script>
export default {

}
</script>

<style scoped>
.modal {
	width: 24rem;
  color: #33465E;
  background-color: white;
	position: fixed;
	top: -50%;
	left: 50%;
	transform: translate(-50%, -50%);
  box-shadow: 0 0 1rem rgba(black, 0.1);
	opacity: 1;
	transition: opacity 550ms ease-in-out;
  
  &__article {
    text-align: center;
    padding: 2.5rem;
    
    .modal-title {
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
    }
  }
  
  &__footer {
    width: 100%;
    height: 3rem;
  }
  
  &.in {
		opacity: 1;
		top: 50%;
	}
}
</style>