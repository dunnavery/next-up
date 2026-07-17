// Server Component in Next.js
interface BookCardProps {
    title: string;
    author: string;
    rating: number;
}

export default function BookCard({ title, author, rating }: BookCardProps) {
    return (
        <div className="p-4 m-2 w-full">
            <p className="font-bold">{title}</p>
            <p>{author}</p>
            <p>Rating: {rating}</p>
        </div>
    );
}