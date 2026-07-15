import { useState } from 'react';
import './Contact.css';

export default function Contact({ profile }) {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });
  const [statusMsg, setStatusMsg] = useState(null); // { type: 'success' | 'error', text: string }
  const [loading, setLoading] = useState(false);

  if (!profile || !profile.email) return null;

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setStatusMsg(null);

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/api/contact/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setStatusMsg({
          type: 'success',
          text: data.message || 'Your message has been sent successfully.',
        });
        setFormData({ name: '', email: '', subject: '', message: '' });
      } else {
        // Collect server field validation errors or fallback
        const errText = Object.entries(data)
          .map(([key, val]) => `${key}: ${Array.isArray(val) ? val.join(' ') : val}`)
          .join('\n') || 'Failed to send message.';
        setStatusMsg({
          type: 'error',
          text: errText,
        });
      }
    } catch (err) {
      console.error(err);
      setStatusMsg({
        type: 'error',
        text: 'Connection failed. Please verify the backend is running.',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="section" id="contact">
      <div className="container">
        <div className="accent-line" />
        <h2 className="section-title">Contact</h2>
        <p className="section-subtitle">
          Have an opportunity or question? Feel free to reach out.
        </p>

        <div className="contact-grid">
          <div className="contact-info">
            <div>
              <h3 className="contact-info-title">Let&apos;s Connect</h3>
              <p className="contact-info-text">
                I am currently open to full-time roles and collaborative projects.
                Fill out the form or reach out through my contact details.
              </p>
            </div>

            <div className="contact-methods">
              <div className="contact-method-item">
                <div className="contact-method-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                  </svg>
                </div>
                <div>
                  <div className="contact-method-label">Email</div>
                  <div className="contact-method-value">
                    <a href={`mailto:${profile.email}`}>{profile.email}</a>
                  </div>
                </div>
              </div>

              {profile.phone && (
                <div className="contact-method-item">
                  <div className="contact-method-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>
                    </svg>
                  </div>
                  <div>
                    <div className="contact-method-label">Phone</div>
                    <div className="contact-method-value">{profile.phone}</div>
                  </div>
                </div>
              )}

              {profile.location && (
                <div className="contact-method-item">
                  <div className="contact-method-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                      <circle cx="12" cy="10" r="3"/>
                    </svg>
                  </div>
                  <div>
                    <div className="contact-method-label">Location</div>
                    <div className="contact-method-value">{profile.location}</div>
                  </div>
                </div>
              )}
            </div>
          </div>

          <div className="contact-form-container">
            <form onSubmit={handleSubmit} className="contact-form">
              <div className="form-group-row">
                <div className="form-group">
                  <label htmlFor="contact-name" className="form-label">Name</label>
                  <input
                    id="contact-name"
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="form-input"
                    placeholder="John Doe"
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="contact-email" className="form-label">Email</label>
                  <input
                    id="contact-email"
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    className="form-input"
                    placeholder="john@example.com"
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="contact-subject" className="form-label">Subject</label>
                <input
                  id="contact-subject"
                  type="text"
                  name="subject"
                  value={formData.subject}
                  onChange={handleChange}
                  className="form-input"
                  placeholder="Inquiry / Opportunity"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="contact-message" className="form-label">Message</label>
                <textarea
                  id="contact-message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  className="form-textarea"
                  placeholder="Hi Suraj, I'd like to talk about..."
                  required
                />
              </div>

              {statusMsg && (
                <div className={`form-status-message ${statusMsg.type}`}>
                  {statusMsg.text}
                </div>
              )}

              <button
                type="submit"
                disabled={loading}
                className="form-submit-btn"
              >
                {loading ? 'Sending...' : 'Send Message'}
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}
