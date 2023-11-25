export type Entry = {
	id: string;
	sentiment: number; // A number from 1 to 5
	created_at: Date;
	body: string;
};

export type Entries = Array<Entry>;
