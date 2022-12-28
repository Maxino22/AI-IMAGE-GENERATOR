<template>
	<main>
		<section class="showcase">
			<form @submit.prevent="onSubmit">
				<h1>Describe An Image</h1>
				<div class="form-control">
					<input type="text" v-model="imagePrompt" placeholder="Enter Text" />
				</div>
				<!-- size -->
				<div class="form-control">
					<select name="size" v-model="imageSize">
						<option disabled value="small">Please select size</option>
						<option value="small">Small</option>
						<option value="medium" selected>Medium</option>
						<option value="large">Large</option>
					</select>
				</div>
				<p v-if="formError" class="error">
					Did you forget to imput description or size
				</p>
				<button type="submit" class="btn">Generate</button>
			</form>
		</section>
		<teleport to=".load">
			<div v-if="showSpinner" class="spinner"></div>
		</teleport>

		<ImageView :img-url="imgUrl" :error-message="errorMsg" />
	</main>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import ImageView from './ImageView.vue'

const imagePrompt = ref('')
const imageSize = ref('medium')
const formError = ref(false)
const showSpinner = ref(false)

const imgUrl = ref('')
const errorMsg = ref('')

function onSubmit() {
	if (imagePrompt === '' || imageSize === '') {
		formError.value = true
	}
	generateImageRequest()
}

async function generateImageRequest() {
	try {
		viewSpinner()
		const response = await fetch('https://ai.maxino.xyz/generateimage', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				prompt: imagePrompt.value,
				size: imageSize.value,
			}),
		})

		if (!response.ok) {
			hideSpinner()
			throw new Error('That image could not be generated')
		}

		const data = await response.json()
		imgUrl.value = data.url
		hideSpinner()
	} catch (error) {
		hideSpinner()
		console.log(error)
		errorMsg.value = 'That image could not be generated'
	}
}

function viewSpinner() {
	showSpinner.value = true
}
function hideSpinner() {
	showSpinner.value = false
}
</script>
