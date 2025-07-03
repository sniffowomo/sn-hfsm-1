import { motion } from 'framer-motion';
import { Building, MapPin, Calendar } from 'lucide-react';
import { cvData } from '../data/cvData';

const Experience = () => {
  const { experience } = cvData;

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
    hidden: { opacity: 0, x: -100 },
    visible: { 
      opacity: 1, 
      x: 0,
      transition: { duration: 0.6 }
    }
  };

  return (
    <motion.section
      className="experience-section"
      variants={containerVariants}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.2 }}
    >
      <div className="container">
        <motion.h2 className="section-title neon-text" variants={itemVariants}>
          Experience
        </motion.h2>
        
        <div className="timeline">
          {experience.map((job, index) => (
            <motion.div
              key={index}
              className="timeline-item"
              variants={itemVariants}
              whileHover={{ scale: 1.01 }}
            >
              <div className="timeline-marker">
                <div className="timeline-dot"></div>
                {index < experience.length - 1 && <div className="timeline-line"></div>}
              </div>
              
              <motion.div 
                className="cyber-card timeline-content"
                whileHover={{
                  borderColor: '#ff0080',
                  boxShadow: '0 0 30px rgba(255, 0, 128, 0.5)'
                }}
              >
                <div className="job-header">
                  <h3 className="job-position">{job.position}</h3>
                  <div className="job-meta">
                    <div className="job-company">
                      <Building size={16} />
                      <span>{job.company}</span>
                    </div>
                    <div className="job-period">
                      <Calendar size={16} />
                      <span>{job.period}</span>
                    </div>
                    <div className="job-location">
                      <MapPin size={16} />
                      <span>{job.location}</span>
                    </div>
                  </div>
                </div>
                
                <ul className="job-achievements">
                  {job.achievements.map((achievement, achievementIndex) => (
                    <motion.li
                      key={achievementIndex}
                      initial={{ opacity: 0, x: -20 }}
                      whileInView={{ 
                        opacity: 1, 
                        x: 0,
                        transition: { 
                          delay: achievementIndex * 0.1,
                          duration: 0.4
                        }
                      }}
                      viewport={{ once: true }}
                    >
                      {achievement}
                    </motion.li>
                  ))}
                </ul>
              </motion.div>
            </motion.div>
          ))}
        </div>
      </div>
    </motion.section>
  );
};

export default Experience;