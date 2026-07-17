// Server Component in Next.js
interface BookCardProps {
    title: string;
    author: string;
    rating: number;
}

export default function BookCard({ title, author, rating }: BookCardProps) {
    return (
        <div>
            <h1>{title}</h1>
            <h2>{author}</h2>
            <p>Rating: {rating}</p>
        </div>
    );
}