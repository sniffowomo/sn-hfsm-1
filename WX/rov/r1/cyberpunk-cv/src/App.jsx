import { motion } from 'framer-motion';
import Navigation from './components/Navigation';
import Header from './components/Header';
import About from './components/About';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Education from './components/Education';
import './styles/cyberpunk.css';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="grid-overlay"></div>
      <Navigation />
      <main>
        <Header />
        <About />
        <Experience />
        <Projects />
        <Education />
      </main>
      
      {/* Floating particles effect */}
      <div className="particles">
        {[...Array(8)].map((_, i) => (
          <motion.div
            key={i}
            className="particle"
            animate={{
              y: [-10, -30, -10],
              x: [0, Math.random() * 20 - 10, 0],
              opacity: [0.2, 0.6, 0.2],
            }}
            transition={{
              duration: Math.random() * 4 + 6,
              repeat: Infinity,
              delay: Math.random() * 3,
              ease: "easeInOut",
            }}
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
