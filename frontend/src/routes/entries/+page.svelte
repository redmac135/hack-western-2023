<script lang="ts">
	import Tmp from '$lib/components/Tmp.svelte';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	export let data;
	let activatepulse: boolean = false;

	// converts 1-5 sentiement score to text
	function sentimentToText(sentiment: number): string {
		if (sentiment === 0) {
			return 'Neutral';
		} else if (sentiment > 0) {
			return 'Positive';
		} else {
			return 'Negative';
		}
	}

	function pulseNewEntry() {
		let newentry: string | null = $page.url.searchParams.get('newentry');
		if (!newentry) return;
		activatepulse = true;
	}

	onMount(() => {
		pulseNewEntry();
	});
</script>

<Tmp />
<h1>Entries</h1>

<section>
	{#each data.entries as entry}
		<div class:newentry={activatepulse}>
			<h2>{entry.created_at}</h2>
			<h3>Sentiment: {sentimentToText(entry.sentiment)}</h3>
			<p>{entry.content}</p>
		</div>
	{/each}
</section>

<style>
	h1 {
		font-family: 'Open Sans', sans-serif;
		text-align: center;
		color: #333;
	}

	div {
		background-color: #fff;
		border: 1px solid #ddd;
		margin: 10px;
		padding: 15px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}

	h2 {
		font-family: 'Open Sans', sans-serif;
		color: #333;
	}

	h3 {
		font-family: 'Open Sans', sans-serif;
		color: #0066cc;
	}

	p {
		font-family: 'Open Sans', sans-serif;
		color: #555;
	}

	.newentry:first-child {
		animation: pulse 0.8s ease-in-out;
		animation-iteration-count: 1;
	}

	@keyframes pulse {
		0% {
			background-color: white;
		}
		70% {
			background-color: gold;
		}
		100% {
			background-color: white;
		}
	}
</style>
