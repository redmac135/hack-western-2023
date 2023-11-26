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
		}).then(() => goto('/entries/?newentry=true'));
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
<section>
	<input
		type="checkbox"
		name="record"
		id="record"
		bind:checked={recording}
		on:change={handleRecordingToggle}
	/>
	<label for="record">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="100"
			height="100"
			viewBox="0 0 100 100"
			id="microphone"
			><g
				><path
					d="M52 75.9V86h14c1.1 0 2 .9 2 2s-.9 2-2 2H34c-1.1 0-2-.9-2-2s.9-2 2-2h14V75.9c-13.4-1-24-12.3-24-25.9 0-1.1.9-2 2-2s2 .9 2 2c0 12.1 9.9 22 22 22s22-9.9 22-22c0-1.1.9-2 2-2s2 .9 2 2c0 13.7-10.6 24.9-24 25.9zM65 25v25c0 8.3-6.7 15-15 15s-15-6.7-15-15V25c0-8.3 6.7-15 15-15s15 6.7 15 15zm-4 0c0-6.1-4.9-11-11-11s-11 4.9-11 11v25c0 6.1 4.9 11 11 11s11-4.9 11-11V25z"
				/></g
			><g><path fill="#00F" d="M1084-650v1684H-700V-650h1784m8-8H-708v1700h1800V-658z" /></g></svg
		>
	</label>
</section>

<style>
	/* then your styles go at the bottom in a "style" tag */

	section {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

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
		display: none;
	}

	/* Style the checkbox container */
	.checkbox-container {
		display: flex;
		align-items: center;
	}

	/* Style the checkbox */
	input[type='checkbox'] + label {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 10rem;
		height: 10rem;
		border-radius: 999rem;
		background-color: grey;
		border: 2px solid #ccc;
		position: relative;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	input[type='checkbox']:checked + label {
		background-color: rgb(194, 33, 33);
		border: 1px solid red;
		animation-name: pulse;
		animation-duration: 1.5s;
		animation-iteration-count: infinite;
		animation-timing-function: linear;
	}

	input[type='checkbox']:checked:before + label {
		transform: translateX(20px);
		border: 1px solid #45a049;
	}

	@keyframes pulse {
		0% {
			box-shadow: 0px 0px 5px 0px rgba(173, 0, 0, 0.3);
		}
		65% {
			box-shadow: 0px 0px 5px 13px rgba(173, 0, 0, 0.3);
		}
		90% {
			box-shadow: 0px 0px 5px 13px rgba(173, 0, 0, 0);
		}
	}
</style>
