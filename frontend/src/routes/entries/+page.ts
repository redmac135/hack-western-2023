import type { Entries } from '$lib/schema';
import { PUBLIC_BACKEND_URL } from '$env/static/public';

export async function load({ fetch }): Promise<{ entries: Entries }> {
	const res = await fetch(`${PUBLIC_BACKEND_URL}/entries/list/`);
	const data = await res.json();
	data.sort((a, b) => ('' + b.created_at).localeCompare('' + a.created_at));
	return { entries: data };
}

// export function load() {
// 	return {
// 		entries: [
// 			{
// 				id: '1',
// 				sentiment: 0.5,
// 				magnitude: 0.5,
// 				created_at: new Date().toString(),
// 				content: 'This is a test entry'
// 			},
// 			{
// 				id: '2',
// 				sentiment: 0.5,
// 				magnitude: 0.5,
// 				created_at: new Date().toString(),
// 				content: 'This is a test entry'
// 			}
// 		]
// 	};
// }
