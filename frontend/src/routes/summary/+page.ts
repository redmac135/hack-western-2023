import type { Entries } from '$lib/schema';
import { PUBLIC_BACKEND_URL } from '$env/static/public';

export async function load({ fetch }) {
	const res = await fetch(`${PUBLIC_BACKEND_URL}/entries/list/`);
	const data = await res.json();
	data.sort((a, b) => a.sentiment - b.sentiment);
	let average_sentiment = data.reduce((total, next) => total + next.sentiment, 0) / data.length;
	return {
		average_sentiment: average_sentiment,
		most_positive: data[data.length - 1],
		most_negative: data[0]
	};
}

// export function load() {
// 	return {
// 		average_sentiment: 0.5,
// 		most_positive: {
// 			id: '1',
// 			sentiment: 0.5,
// 			magnitude: 0.5,
// 			created_at: new Date().toString(),
// 			content: 'This is a test entry'
// 		},
// 		most_negative: {
// 			id: '2',
// 			sentiment: 0.5,
// 			magnitude: 0.5,
// 			created_at: new Date().toString(),
// 			content: 'This is a test entry'
// 		}
// 	};
// }
