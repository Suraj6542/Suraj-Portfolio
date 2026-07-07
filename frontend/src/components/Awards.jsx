import { useState } from 'react';
import './Awards.css';

export default function Awards({ awards }) {
  const [openAwardId, setOpenAwardId] = useState(null);

  if (!awards || awards.length === 0) return null;

  const toggleAwardImages = (awardId) => {
    setOpenAwardId((currentId) => (currentId === awardId ? null : awardId));
  };

  return (
    <section className="awards section" id="awards">
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">Honors &amp; Awards</h2>
        <p className="section-subtitle">
          Recognition and achievements in tech and academic competitions.
        </p>

        <div className="awards-list">
          {awards.map((award) => (
            <div key={award.id} className="award-item">
              <div className="award-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="8" r="7"/>
                  <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
                </svg>
              </div>
              <div className="award-content">
                <div className="award-title">{award.title}</div>
                {award.description && (
                  <p className="award-description">{award.description}</p>
                )}
                {award.date && <div className="award-date">{award.date}</div>}

                {award.title.includes('Database Management Competition') && (
                  <button
                    type="button"
                    className="award-toggle-button"
                    onClick={() => toggleAwardImages(award.id)}
                  >
                    {openAwardId === award.id ? 'Hide Award Images' : 'View Award Images'}
                  </button>
                )}

                {openAwardId === award.id && (
                  <div className="award-image-grid">
                    <div className="award-image-card">
                      <img src="/award-1.jpg" alt="Award ceremony photo" />
                    </div>
                    <div className="award-image-card">
                      <img src="/award-2.jpg" alt="Award trophy photo" />
                    </div>
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
