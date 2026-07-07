import './Leadership.css';

export default function Leadership({ leadership }) {
  if (!leadership || leadership.length === 0) return null;

  return (
    <section className="section" id="leadership">
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">Leadership &amp; Volunteering</h2>
        <p className="section-subtitle">
          Community involvement and extracurricular contributions.
        </p>

        {leadership.map((item) => (
          <div key={item.id} className="leadership-card">
            <div className="leadership-header">
              <div>
                <div className="leadership-role">{item.role}</div>
                <div className="leadership-org">{item.organization}</div>
              </div>
              <div className="leadership-meta">
                {item.location && (
                  <div className="leadership-location">{item.location}</div>
                )}
                <div className="leadership-date">
                  {item.start_date} — {item.end_date}
                </div>
              </div>
            </div>

            {item.bullets && item.bullets.length > 0 && (
              <div className="leadership-bullets">
                {item.bullets.map((bullet) => (
                  <div key={bullet.id} className="leadership-bullet">
                    {bullet.title && <strong>{bullet.title}: </strong>}
                    {bullet.content}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}
