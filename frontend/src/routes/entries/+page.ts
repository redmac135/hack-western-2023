import type { Entries } from '$lib/schema';
import { PUBLIC_BACKEND_URL } from '$env/static/public';

// Temporary test data
export async function load({ fetch }): Promise<{ entries: Entries }> {
	const res = await fetch(`${PUBLIC_BACKEND_URL}/entries/list/`);
	const data = await res.json();
	data.sort((a, b) => ('' + b.created_at).localeCompare('' + a.created_at));
	return { entries: data };
}
