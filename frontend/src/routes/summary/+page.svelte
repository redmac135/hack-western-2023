<script lang="ts">
	export let data;
</script>

<main>
	<div>
		<h2>Average Mood</h2>
		<p>{data.average_sentiment}</p>
	</div>
	<div>
		<h2>Most Positive</h2>
		<p>{data.most_positive.created_at}</p>
		<p>{data.most_positive.sentiment}</p>
	</div>
	<div>
		<h2>Most Negative</h2>
		<p>{data.most_negative.created_at}</p>
		<p>{data.most_negative.sentiment}</p>
	</div>
</main>
