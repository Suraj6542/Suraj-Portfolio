import { useEffect, useRef, useState } from 'react';
import './Skills.css';

export default function Skills({ skillCategories }) {
  const [visible, setVisible] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          observer.disconnect();
        }
      },
      { threshold: 0.2 }
    );

    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  if (!skillCategories || skillCategories.length === 0) return null;

  return (
    <section className="section" id="skills" ref={ref}>
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">Skills &amp; Expertise</h2>
        <p className="section-subtitle">
          Technologies and tools I work with on a daily basis.
        </p>

        <div className="skills-grid">
          {skillCategories.map((category) => (
            <div key={category.id} className="skill-category-card">
              <div className="skill-category-name">{category.name}</div>
              <div className="skill-list">
                {category.skills.map((skill) => (
                  <div key={skill.id} className="skill-item">
                    <div className="skill-header">
                      <span className="skill-name">{skill.name}</span>
                      <span className="skill-percentage">{skill.proficiency}%</span>
                    </div>
                    <div className="skill-bar">
                      <div
                        className="skill-bar-fill"
                        style={{ width: visible ? `${skill.proficiency}%` : '0%' }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
