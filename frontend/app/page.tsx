import BookCard from "@/components/BookCard";

export default function Home() {
  return (
    <main>
      <h1 className="p-4 m-2 text-2xl font-bold">Books</h1>
      <BookCard title="The Great Gatsby" author="F. Scott Fitzgerald" rating={4.5} />
      <BookCard title="To Kill a Mockingbird" author="Harper Lee" rating={4.8} />
    </main>
  );
}
