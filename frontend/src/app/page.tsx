export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-6">
      <div className="max-w-md w-full bg-white rounded-2xl shadow-lg p-8 text-center">
        <h1 className="text-3xl font-bold text-orange-500 mb-4">
          🍳 Recipe Platform
        </h1>
        <p className="text-gray-600 mb-6">
          Frontend Next.js đã kết nối thành công. 
          Sẵn sàng xây dựng các tính năng: Công thức, Tủ lạnh ảo và Danh sách đi chợ.
        </p>
        <div className="flex gap-4 justify-center">
          <button className="bg-orange-500 text-white px-6 py-2 rounded-full font-medium hover:bg-orange-600 transition">
            Khám phá món ăn
          </button>
          <button className="bg-gray-100 text-gray-700 px-6 py-2 rounded-full font-medium hover:bg-gray-200 transition">
            Đăng nhập
          </button>
        </div>
      </div>
    </main>
  );
}