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
</style>
