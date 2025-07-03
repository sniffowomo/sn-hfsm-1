import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Globe, Github, Linkedin } from 'lucide-react';
import { cvData } from '../data/cvData';

const Header = () => {
  const { personal } = cvData;

  const containerVariants = {
    hidden: { opacity: 0, y: -50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.8,
        staggerChildren: 0.2
      }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: -20 },
    visible: { opacity: 1, y: 0 }
  };

  return (
    <motion.header
      className="header-section"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      <div className="container">
        <motion.div className="hero-content" variants={itemVariants}>
          <motion.h1 
            className="hero-name neon-text glitch" 
            data-text={personal.name}
            variants={itemVariants}
          >
            {personal.name}
          </motion.h1>
          
          <motion.h2 className="hero-title" variants={itemVariants}>
            {personal.title}
          </motion.h2>
          
          <motion.p className="hero-subtitle" variants={itemVariants}>
            {personal.subtitle}
          </motion.p>
        </motion.div>

        <motion.div className="contact-grid" variants={itemVariants}>
          <motion.a 
            href={`mailto:${personal.email}`}
            className="contact-item"
            whileHover={{ scale: 1.02, color: '#00ffff' }}
            whileTap={{ scale: 0.98 }}
          >
            <Mail size={20} />
            <span>{personal.email}</span>
          </motion.a>
          
          <motion.a 
            href={`tel:${personal.phone}`}
            className="contact-item"
            whileHover={{ scale: 1.02, color: '#00ffff' }}
            whileTap={{ scale: 0.98 }}
          >
            <Phone size={20} />
            <span>{personal.phone}</span>
          </motion.a>
          
          <motion.div 
            className="contact-item"
            whileHover={{ scale: 1.02, color: '#00ffff' }}
          >
            <MapPin size={20} />
            <span>{personal.location}</span>
          </motion.div>
          
          <motion.a 
            href={`https://${personal.website}`}
            target="_blank"
            rel="noopener noreferrer"
            className="contact-item"
            whileHover={{ scale: 1.02, color: '#00ffff' }}
            whileTap={{ scale: 0.98 }}
          >
            <Globe size={20} />
            <span>{personal.website}</span>
          </motion.a>
          
          <motion.a 
            href={`https://${personal.github}`}
            target="_blank"
            rel="noopener noreferrer"
            className="contact-item"
            whileHover={{ scale: 1.02, color: '#00ffff' }}
            whileTap={{ scale: 0.98 }}
          >
            <Github size={20} />
            <span>GitHub</span>
          </motion.a>
          
          <motion.a 
            href={`https://${personal.linkedin}`}
            target="_blank"
            rel="noopener noreferrer"
            className="contact-item"
            whileHover={{ scale: 1.02, color: '#00ffff' }}
            whileTap={{ scale: 0.98 }}
          >
            <Linkedin size={20} />
            <span>LinkedIn</span>
          </motion.a>
        </motion.div>
      </div>
    </motion.header>
  );
};

export default Header;