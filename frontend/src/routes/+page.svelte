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
		// Tmp user id
		formData.append('useruid', '1');
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
<h1>Talk About Your Day...</h1>
<p>Start Recording</p>
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
		font-family: 'Open Sans', sans-serif;
		text-align: center;
		color: #333;
	}

	p {
		font-family: 'Open Sans', sans-serif;
		color: #0066cc;
	}

	input {
		margin-top: 10px;
		margin-bottom: 20px;
	}

	/* Style the checkbox container */
	.checkbox-container {
		display: flex;
		align-items: center;
	}

	/* Style the checkbox */
	input[type='checkbox'] {
		appearance: none;
		width: 100px;
		height: 100px;
		background-color: #eee;
		border: 2px solid #ccc;
		display: inline-block;
		position: relative;
		border-radius: 3px;
		cursor: pointer;
	}

	input[type='checkbox']:checked {
		background-color: #4caf50;
		border: 1px solid #45a049;
	}

	input[type='checkbox']:checked:before {
		transform: translateX(20px);
		border: 1px solid #45a049;
	}

	/* Additional styling for the recording status */
	p.recording {
		color: red;
		font-weight: bold;
		margin-top: 10px;
	}
</style>
