import "./App.css"

function App() {
  return (
    <>
      <div className="flex items-center justify-between min-h-screen bg-slate-950 text-green-500 p-8">
        <TwoColumnLayout left={<MainText />} right={<Form1 />} />
      </div>
    </>
  )
}

export default App
