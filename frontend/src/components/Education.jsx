import './Education.css';

export default function Education({ education }) {
  if (!education || education.length === 0) return null;

  return (
    <section className="education section" id="education">
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">Education</h2>
        <p className="section-subtitle">
          My academic background and qualifications.
        </p>

        {education.map((edu) => (
          <div key={edu.id} className="education-card">
            <div className="education-icon">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                <path d="M6 12v5c3 3 9 3 12 0v-5"/>
              </svg>
            </div>
            <div className="education-info">
              <div className="education-degree">{edu.degree}</div>
              {edu.field_of_study && (
                <div className="education-field">{edu.field_of_study}</div>
              )}
              <div className="education-institution">{edu.institution}</div>
              <span className="education-years">
                {edu.start_year} — {edu.end_year}
              </span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
