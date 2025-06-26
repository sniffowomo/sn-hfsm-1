import { useState } from "react"

export default function MainText() {
  const [count, setCount] = useState(0)

  return (
    <div className="w-full max-w-md px-4 text-center font-fdin ">
      {/* Logo Section */}
      <div className="flex justify-center gap-8 mb-6">
        <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
          <img
            src="/vite.svg"
            className="w-20 h-20 transition-transform hover:scale-110"
            alt="Vite logo"
          />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img
            src="/react.svg"
            className="w-20 h-20 transition-transform hover:scale-110"
            alt="React logo"
          />
        </a>
      </div>

      {/* Title */}
      <h1
        className="font-orb text-4xl font-extrabold mb-6
             hover:text-purple-400 
             hover:scale-110 
             transition-all duration-300 ease-in-out"
      >
        Vite + React
      </h1>

      {/* Counter Button */}
      <div className="card bg-gray-900 p-6 rounded-lg shadow-md text-center mb-6 hover:bg-gray-950 hover:scale-105 transition-all duration-300">
        <button
          onClick={() => setCount((count) => count + 1)}
          className="px-4 py-2 bg-green-600 rounded hover:bg-green-700 transition-colors text-slate-950"
        >
          count is {count}
        </button>
        <p className="mt-4 text-gray-300">
          Edit <code className="bg-gray-700 px-1 rounded">src/App.jsx</code> and
          save to test HMR
        </p>
      </div>

      {/* Footer Text */}
      <p className="text-sm text-green-400 hover:text-rose-400 transition-colors duration-300">
        BootyDancer
      </p>
    </div>
  )
}
