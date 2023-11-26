<nav>
	<a href="/">Home</a>
	<a href="/entries">About</a>
	<a href="/summary">Contact</a>
</nav>
<slot />

<style>
	nav {
		display: flex;
		justify-content: right;
		align-items: center;
		width: 100%;
		height: 4rem;
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
