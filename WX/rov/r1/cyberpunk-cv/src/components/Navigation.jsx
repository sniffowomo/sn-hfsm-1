import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';

const Navigation = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('header');

  const navItems = [
    { id: 'header', label: 'Home' },
    { id: 'about', label: 'About' },
    { id: 'experience', label: 'Experience' },
    { id: 'projects', label: 'Projects' },
    { id: 'education', label: 'Education' }
  ];

  useEffect(() => {
    const handleScroll = () => {
      const sections = navItems.map(item => document.querySelector(`.${item.id}-section`));
      const scrollPosition = window.scrollY + 100;

      sections.forEach((section, index) => {
        if (section) {
          const sectionTop = section.offsetTop;
          const sectionBottom = sectionTop + section.offsetHeight;
          
          if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
            setActiveSection(navItems[index].id);
          }
        }
      });
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const section = document.querySelector(`.${sectionId}-section`);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
    setIsOpen(false);
  };

  return (
    <motion.nav
      className="navigation"
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.8 }}
    >
      <div className="nav-container">
        <motion.div
          className="nav-logo"
          whileHover={{ scale: 1.05, color: '#00ffff' }}
        >
          <span className="neon-text">AC</span>
        </motion.div>

        {/* Desktop Navigation */}
        <div className="nav-menu desktop-menu">
          {navItems.map((item) => (
            <motion.button
              key={item.id}
              className={`nav-item ${activeSection === item.id ? 'active' : ''}`}
              onClick={() => scrollToSection(item.id)}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              {item.label}
            </motion.button>
          ))}
        </div>

        {/* Mobile Menu Toggle */}
        <motion.button
          className="mobile-menu-toggle"
          onClick={() => setIsOpen(!isOpen)}
          whileTap={{ scale: 0.9 }}
        >
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </motion.button>

        {/* Mobile Navigation */}
        <motion.div
          className={`nav-menu mobile-menu ${isOpen ? 'open' : ''}`}
          initial={{ opacity: 0, x: 300 }}
          animate={{ 
            opacity: isOpen ? 1 : 0, 
            x: isOpen ? 0 : 300 
          }}
          transition={{ duration: 0.3 }}
        >
          {navItems.map((item, index) => (
            <motion.button
              key={item.id}
              className={`nav-item ${activeSection === item.id ? 'active' : ''}`}
              onClick={() => scrollToSection(item.id)}
              initial={{ opacity: 0, x: 50 }}
              animate={{ 
                opacity: isOpen ? 1 : 0, 
                x: isOpen ? 0 : 50 
              }}
              transition={{ 
                duration: 0.3, 
                delay: isOpen ? index * 0.1 : 0 
              }}
            >
              {item.label}
            </motion.button>
          ))}
        </motion.div>
      </div>
    </motion.nav>
  );
};

export default Navigation;