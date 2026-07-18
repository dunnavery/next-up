import BookCard from "@/components/BookCard";

export default function Home() {
  const books = [
      { title: "To Kill a Mockingbird", author: "Harper Lee", rating: 4.8 },
      { title: "1984", author: "George Orwell", rating: 4.7 },
      { title: "The Great Gatsby", author: "F. Scott Fitzgerald", rating: 4.6 },
      { title: "Pride and Prejudice", author: "Jane Austen", rating: 4.5 },
      { title: "The Catcher in the Rye", author: "J.D. Salinger", rating: 4.4 },
  ]

  return (
    <main>
      <div className="mx-auto flex items-center">
        <div>
          <h1 className="p-4 m-2 text-2xl font-bold">Books</h1>
          <BookCard books={books} />
        </div>
      </div>
    </main>
  );
}
