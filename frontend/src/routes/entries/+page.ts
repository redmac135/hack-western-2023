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

export function load(): { entries: Entries } {
	return { entries: tmp_data };
}
