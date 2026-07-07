import { useState } from 'react';
import './Experience.css';

export default function Experience({ experiences }) {
  const [showExperienceImages, setShowExperienceImages] = useState(false);

  if (!experiences || experiences.length === 0) return null;

  return (
    <section className="experience section" id="experience">
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">Professional Experience</h2>
        <p className="section-subtitle">
          My career journey and key contributions.
        </p>

        <button
          type="button"
          className="experience-toggle-button"
          onClick={() => setShowExperienceImages((current) => !current)}
        >
          {showExperienceImages ? 'Hide Experience Images' : 'View Experience Images'}
        </button>

        {showExperienceImages && (
          <div className="experience-image-grid">
            <div className="experience-image-card">
              <img src="/experience-1.jpg" alt="Work experience photo 1" />
            </div>
            <div className="experience-image-card">
              <img src="/experience-2.jpg" alt="Work experience photo 2" />
            </div>
          </div>
        )}

        <div className="experience-timeline">
          {experiences.map((exp) => (
            <div key={exp.id} className="experience-card">
              <div className="experience-card-inner">
                <div className="experience-header">
                  <div>
                    <div className="experience-role">{exp.role}</div>
                    <div className="experience-company">{exp.company}</div>
                  </div>
                  <span className="experience-date">
                    {exp.start_date} — {exp.end_date}
                  </span>
                </div>

                {exp.description && (
                  <p className="experience-description">{exp.description}</p>
                )}

                {exp.bullets && exp.bullets.length > 0 && (
                  <div className="experience-bullets">
                    {exp.bullets.map((bullet) => (
                      <div key={bullet.id} className="experience-bullet">
                        {bullet.title && (
                          <div className="experience-bullet-title">
                            {bullet.title}
                          </div>
                        )}
                        <p className="experience-bullet-content">
                          {bullet.content}
                        </p>
                        {bullet.skills_used && (
                          <div className="experience-skills">
                            {bullet.skills_used.split(',').map((skill, i) => (
                              <span key={i} className="experience-skill-tag">
                                {skill.trim()}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
