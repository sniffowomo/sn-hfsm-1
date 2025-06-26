export default function TwoColumnLayout({ left, right }) {
  return (
    <div className="min-h-screen bg-slate-950 text-green-500 p-4 md:p-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center justify-center max-w-6xl mx-auto">
        {/* Left Side */}
        <div className="flex justify-center">
          <div className="w-full max-w-lg">{left}</div>
        </div>

        {/* Right Side */}
        <div className="flex justify-center">
          <div className="w-full max-w-md">{right}</div>
        </div>
      </div>
    </div>
  )
}
