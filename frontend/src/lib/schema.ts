export type Entry = {
	id: string;
	sentiment: number;
	magnitude: number;
	created_at: Date;
	content: string;
};

export type Entries = Array<Entry>;
