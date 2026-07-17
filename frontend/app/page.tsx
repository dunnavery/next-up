import BookCard from "@/components/BookCard";

export default function Home() {
  return (
    <main>
      <BookCard title="The Great Gatsby" author="F. Scott Fitzgerald" rating={4.5} />
    </main>
  );
}
