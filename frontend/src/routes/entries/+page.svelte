<script lang="ts">
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

<h1>Entries</h1>

{#each data.entries as entry}
	<div>
		<h2>{entry.created_at.toLocaleDateString('en-US')}</h2>
		<h3>{sentimentToText(entry.sentiment)}</h3>
		<p>{entry.body}</p>
	</div>
{/each}

<style>
	/* style goes here */
	@ import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap");

	body {
		font-family: "Poppins", sans-serif;
		background-color: #f4f4f4;
		margin: 0;
		padding: 0;

	}

	h1 {
		text-align: center;
		color: #333;
	}

	div {
		border: 1px solid #ddd;
		margin: 10px;
		padding: 10px;
	}

	h2 {
		color: #555;
	}

	h3 {
		color: green
	}

	p {
		color: #333;
	}
</style>
