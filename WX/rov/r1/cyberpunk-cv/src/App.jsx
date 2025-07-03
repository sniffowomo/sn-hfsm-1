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
        {[...Array(20)].map((_, i) => (
          <motion.div
            key={i}
            className="particle"
            animate={{
              y: [-20, -100, -20],
              x: [0, Math.random() * 100 - 50, 0],
              opacity: [0, 1, 0],
            }}
            transition={{
              duration: Math.random() * 3 + 2,
              repeat: Infinity,
              delay: Math.random() * 2,
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
