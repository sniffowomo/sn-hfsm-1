import { motion } from 'framer-motion';
import { ExternalLink, Github } from 'lucide-react';
import { cvData } from '../data/cvData';

const Projects = () => {
  const { projects } = cvData;

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2
      }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: { duration: 0.6 }
    }
  };

  return (
    <motion.section
      className="projects-section"
      variants={containerVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.2 }}
    >
      <div className="container">
        <motion.h2 className="section-title neon-text" variants={itemVariants}>
          Projects
        </motion.h2>
        
        <motion.div className="projects-grid" variants={containerVariants}>
          {projects.map((project, index) => (
            <motion.div
              key={index}
              className="cyber-card project-card"
              variants={itemVariants}
              whileHover={{ 
                scale: 1.05,
                rotateY: 5,
                boxShadow: '0 0 40px rgba(128, 0, 255, 0.6)'
              }}
              whileTap={{ scale: 0.98 }}
            >
              <div className="project-header">
                <h3 className="project-name">{project.name}</h3>
                <motion.a
                  href={`https://${project.link}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="project-link"
                  whileHover={{ scale: 1.2, color: '#00ffff' }}
                  whileTap={{ scale: 0.9 }}
                >
                  <ExternalLink size={20} />
                </motion.a>
              </div>
              
              <p className="project-description">{project.description}</p>
              
              <div className="project-technologies">
                {project.technologies.map((tech, techIndex) => (
                  <motion.span
                    key={tech}
                    className="tech-tag"
                    initial={{ opacity: 0, scale: 0 }}
                    whileInView={{ 
                      opacity: 1, 
                      scale: 1,
                      transition: { 
                        delay: techIndex * 0.1,
                        duration: 0.3,
                        type: "spring",
                        stiffness: 200
                      }
                    }}
                    whileHover={{ 
                      scale: 1.1,
                      backgroundColor: 'rgba(0, 255, 255, 0.2)',
                      color: '#00ffff'
                    }}
                    viewport={{ once: true }}
                  >
                    {tech}
                  </motion.span>
                ))}
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </motion.section>
  );
};

export default Projects;