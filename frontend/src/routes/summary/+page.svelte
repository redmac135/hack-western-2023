<script lang="ts">
	export let data;
</script>

<main>
	<h1>Summary</h1>
	<div>
		<h2>Average Mood</h2>
		<p>{data.average_sentiment}</p>
	</div>
	<div>
		<h2>Most Positive Entry</h2>
		<p>{data.most_positive.created_at.toLocaleDateString('en-US')}</p>
		<p>{data.most_positive.sentiment}</p>
	</div>
	<div>
		<h2>Most Negative Entry</h2>
		<p>{data.most_negative.created_at.toLocaleDateString('en-US')}</p>
		<p>{data.most_negative.sentiment}</p>
	</div>
</main>

<style>
	h1 {
		font-family: "Open Sans", sans-serif;
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

	h1 {
		font-family: "Open Sans", sans-serif;
		text-align: center;
		color: #333;
	}

	h2 {
		font-family: "Open Sans", sans-serif;
		color: #333;
	}

	h3 {
		font-family: "Open Sans", sans-serif;
		color: #0066cc;
	}

	p {
		font-family: "Open Sans", sans-serif;
		color: #0066cc;
	}
</style>
