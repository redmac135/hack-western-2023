import type { Entries } from '$lib/schema';

// Temporary test data
const tmp_data: Entries = [
	{
		id: '1',
		sentiment: 5,
		created_at: new Date(),
		body: 'This is a test entry.'
	},
	{
		id: '2',
		sentiment: 3,
		created_at: new Date(),
		body: 'This is another test entry.'
	}
];

tmp_data.sort((a, b) => a.sentiment - b.sentiment);
let average_sentiment =
	tmp_data.reduce((total, next) => total + next.sentiment, 0) / tmp_data.length;

export function load() {
	return {
		average_sentiment: average_sentiment,
		most_positive: tmp_data[tmp_data.length - 1],
		most_negative: tmp_data[0]
	};
}
