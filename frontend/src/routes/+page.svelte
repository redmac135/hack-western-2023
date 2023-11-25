<script lang="ts">
	import { onMount } from 'svelte';
	import { PUBLIC_BACKEND_URL } from '$env/static/public';
	import { goto } from '$app/navigation';
	let media = [];
	let mediaRecorder = null;
	let recording: boolean;

	async function uploadAudio(blob) {
		const formData = new FormData();
		formData.append('audio', blob);
		return await fetch(`${PUBLIC_BACKEND_URL}entries/create/`, {
			method: 'POST',
			body: formData
		}).then(() => goto('/entries'));
	}

	onMount(async () => {
		const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
		mediaRecorder = new MediaRecorder(stream);
		mediaRecorder.ondataavailable = function (e) {
			media.push(e.data);
		};
		mediaRecorder.onstop = function () {
			const blob = new Blob(media, { type: 'audio/ogg' });
			uploadAudio(blob);
		};
		media = [];
	});
	function startRecording() {
		console.log('started recording');
		mediaRecorder.start();
	}
	function stopRecording() {
		console.log('stopped recording');
		mediaRecorder.stop();
	}

	function handleRecordingToggle() {
		// note: this value is reversed as handle change gets called before bind is called.
		if (recording) {
			startRecording();
		} else {
			stopRecording();
		}
	}
</script>

<!-- you can write any html here -->
<h1>This is my title!</h1>
<p>here's some body tages</p>
<input
	type="checkbox"
	name="record"
	id="record"
	bind:checked={recording}
	on:change={handleRecordingToggle}
/>

<style>
	/* then your styles go at the bottom in a "style" tag */

	h1 {
		color: red;
	}

	p {
		color: blue;
	}
</style>
