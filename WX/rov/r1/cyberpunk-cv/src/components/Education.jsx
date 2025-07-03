import { motion } from 'framer-motion';
import { GraduationCap, Calendar, Award } from 'lucide-react';
import { cvData } from '../data/cvData';

const Education = () => {
  const { education } = cvData;

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.3
      }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, scale: 0.8 },
    visible: { 
      opacity: 1, 
      scale: 1,
      transition: { duration: 0.6 }
    }
  };

  return (
    <motion.section
      className="education-section"
      variants={containerVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.3 }}
    >
      <div className="container">
        <motion.h2 className="section-title neon-text" variants={itemVariants}>
          Education
        </motion.h2>
        
        <motion.div className="education-grid" variants={containerVariants}>
          {education.map((edu, index) => (
            <motion.div
              key={index}
              className="cyber-card education-card"
              variants={itemVariants}
              whileHover={{ 
                scale: 1.03,
                borderColor: '#00ff41',
                boxShadow: '0 0 30px rgba(0, 255, 65, 0.5)'
              }}
            >
              <div className="education-header">
                <GraduationCap className="education-icon" size={24} />
                <h3 className="education-degree">{edu.degree}</h3>
              </div>
              
              <div className="education-details">
                <p className="education-school">{edu.school}</p>
                <div className="education-meta">
                  <div className="education-period">
                    <Calendar size={16} />
                    <span>{edu.period}</span>
                  </div>
                  {edu.gpa && (
                    <div className="education-gpa">
                      <Award size={16} />
                      <span>GPA: {edu.gpa}</span>
                    </div>
                  )}
                </div>
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </motion.section>
  );
};

export default Education;