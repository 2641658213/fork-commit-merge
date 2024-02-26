// NextJS - Easy

export default function Home() {
  const sampleProducts = [
    { name: "Classic T-Shirt", price: 19.99 },
    { name: "Stylish Backpack", price: 39.99 },
    { name: "Wireless Headphones", price: 79.99 }
  ];

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <h1 className="text-4xl font-bold mb-4">Welcome to XYZ Store!</h1>
      <p className="text-lg mb-8">
        Your one-stop shop for the best products in town.
      </p>

      <div className="w-1/2 flex flex-col space-y-4">
        {sampleProducts.map((product, index) => (
          <div
            key={index}
            className="flex justify-between p-4 border rounded shadow"
          >
            <span>{product.name}</span>
            <span>{product.price}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
