<nav>
	<a href="/">Home</a>
	<a href="/entries">Entries</a>
	<a href="/summary">Summary</a>
</nav>
<slot />

<style>
	nav {
		display: flex;
		justify-content: right;
		align-items: center;
		height: 4rem;
		padding-right: 2rem;
	}

	a {
		padding: 0.1rem;
		margin: 0.4rem;
		color: rgb(70, 70, 70);
		text-decoration: none;
		transition: border-bottom 0.3s;
	}

	a:hover {
		border-bottom: 1px solid black;
	}
</style>
