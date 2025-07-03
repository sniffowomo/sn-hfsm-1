import { motion } from 'framer-motion';
import { cvData } from '../data/cvData';

const About = () => {
  const { about } = cvData;

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
    hidden: { opacity: 0, x: -50 },
    visible: { 
      opacity: 1, 
      x: 0,
      transition: { duration: 0.6 }
    }
  };

  const skillVariants = {
    hidden: { opacity: 0, scale: 0.8 },
    visible: { 
      opacity: 1, 
      scale: 1,
      transition: { duration: 0.4 }
    }
  };

  return (
    <motion.section
      className="about-section"
      variants={containerVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.3 }}
    >
      <div className="container">
        <motion.h2 className="section-title neon-text" variants={itemVariants}>
          About Me
        </motion.h2>
        
        <motion.div className="cyber-card about-content" variants={itemVariants}>
          <p className="about-summary">{about.summary}</p>
        </motion.div>

        <motion.div className="skills-grid" variants={itemVariants}>
          {about.skills.map((skillGroup, index) => (
            <motion.div
              key={skillGroup.category}
              className="cyber-card skill-category"
              variants={skillVariants}
              whileHover={{ 
                scale: 1.01,
                boxShadow: "0 0 20px rgba(0, 255, 255, 0.3)"
              }}
            >
              <h3 className="skill-category-title">{skillGroup.category}</h3>
              <div className="skill-items">
                {skillGroup.items.map((skill, skillIndex) => (
                  <motion.span
                    key={skill}
                    className="skill-tag"
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ 
                      opacity: 1, 
                      y: 0,
                      transition: { 
                        delay: skillIndex * 0.1,
                        duration: 0.3
                      }
                    }}
                    whileHover={{ 
                      scale: 1.05,
                      color: '#00ffff',
                      textShadow: '0 0 5px #00ffff'
                    }}
                    viewport={{ once: true }}
                  >
                    {skill}
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

export default About;