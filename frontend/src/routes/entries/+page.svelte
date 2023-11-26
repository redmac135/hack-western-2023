<script lang="ts">
	import Tmp from '$lib/components/Tmp.svelte';
	export let data;

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
</script>

<Tmp />
<h1>Entries</h1>

{#each data.entries as entry}
	<div>
		<h2>{entry.created_at}</h2>
		<h3>Sentiment: {sentimentToText(entry.sentiment)}</h3>
		<p>{entry.content}</p>
	</div>
{/each}

<style>
	/* style goes here */

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
</style>
