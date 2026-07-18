// Server Component in Next.js
interface BookCardProps {
    title: string;
    author: string;
    rating: number;
}

export default function BookCard({ books }: { books: BookCardProps[] }) {
    return (
        <div className="p-4 m-2 w-full">
            {books.map((book: BookCardProps) => (
                <div key={book.title} className="p-4 m-2 border rounded shadow">
                    <h2 className="text-xl font-bold">{book.title}</h2>
                    <p className="text-gray-600">by {book.author}</p>
                    <p className="text-yellow-500">Rating: {book.rating}</p>
                </div>
            ))}
        </div>
    );
}
