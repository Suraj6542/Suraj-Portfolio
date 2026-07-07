import './About.css';

export default function About({ profile }) {
  if (!profile || !profile.full_name) return null;

  return (
    <section className="about section" id="about">
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">About Me</h2>
        <p className="section-subtitle">
          Get to know more about my background and what drives me.
        </p>

        <div className="about-grid">
          <div className="about-text">
            <p>
              I am a <strong>Full-Stack Developer</strong> with over a year of hands-on experience
              building production-grade fintech systems. My expertise spans <strong>React, TypeScript,
              ASP.NET Core, Django,</strong> and <strong>MongoDB</strong>, with a strong focus on
              scalable architecture and clean API design.
            </p>
            <p>
              At <strong>Capsitech IT Services</strong>, I work within the Self Assessment team on
              the Acting Office project, where I have built end-to-end modules for HMRC&apos;s Making Tax
              Digital platform, serving <strong>200+ users</strong> and reducing manual reconciliation
              effort by <strong>70%</strong>.
            </p>
            <p>
              I hold a <strong>B.Tech in Computer Science &amp; Engineering</strong> from Biju Patnaik
              University of Technology and am passionate about building robust, user-centric software
              that solves real-world problems at scale.
            </p>
          </div>

          <div className="about-details">
            <div className="about-detail-card">
              <div className="about-detail-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
              </div>
              <div>
                <div className="about-detail-label">Full Name</div>
                <div className="about-detail-value">{profile.full_name}</div>
              </div>
            </div>

            <div className="about-detail-card">
              <div className="about-detail-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                  <polyline points="22,6 12,13 2,6"/>
                </svg>
              </div>
              <div>
                <div className="about-detail-label">Email</div>
                <div className="about-detail-value">
                  <a href={`mailto:${profile.email}`}>{profile.email}</a>
                </div>
              </div>
            </div>

            <div className="about-detail-card">
              <div className="about-detail-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
              </div>
              <div>
                <div className="about-detail-label">Phone</div>
                <div className="about-detail-value">{profile.phone}</div>
              </div>
            </div>

            <div className="about-detail-card">
              <div className="about-detail-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
              </div>
              <div>
                <div className="about-detail-label">Location</div>
                <div className="about-detail-value">{profile.location}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
