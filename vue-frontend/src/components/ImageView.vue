<template>
	<section class="image">
		<div class="image-container">
			<h2 class="msg">{{ errorMessage }}</h2>
			<img :src="imgUrl" alt="" id="image" />
		</div>
	</section>
</template>

<script setup>
const props = defineProps({
	errorMessage: String,
	imgUrl: String,
})
</script>
