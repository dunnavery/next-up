'use client';

import BookCard from "@/components/BookCard";
import { useEffect, useState } from 'react';

export default function Home() {
  const [backendData, setBackendData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/books')
    .then(response => response.json())
    .then(data => setBackendData(data))
    .catch(error => console.error("Error:", error));
  }, []);

  const books = backendData || [];

  return (
    <main>
      <div className="mx-auto flex items-center">
        <div>
          <h1 className="p-4 m-2 text-2xl font-bold border rounded shadow">Books</h1>
          <BookCard books={books} />
        </div>
      </div>
    </main>
  );
}
