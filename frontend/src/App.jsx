import { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Skills from './components/Skills';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Education from './components/Education';
import Leadership from './components/Leadership';
import Awards from './components/Awards';
import Contact from './components/Contact';
import Footer from './components/Footer';

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPortfolioData = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/portfolio/');
        if (!response.ok) {
          throw new Error('Failed to fetch portfolio data');
        }
        const result = await response.json();
        setData(result);
      } catch (err) {
        console.error(err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolioData();
  }, []);

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <div className="loading-text">Loading Suraj&apos;s Portfolio...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="loading-container">
        <div style={{ color: 'var(--color-error)', fontSize: 'var(--font-size-lg)', fontWeight: 'bold' }}>
          Error
        </div>
        <div style={{ color: 'var(--color-text-secondary)', textAlign: 'center', maxWidth: '400px' }}>
          Could not establish connection with backend. Make sure the Django server is running.
        </div>
        <button 
          onClick={() => window.location.reload()}
          style={{
            marginTop: 'var(--spacing-md)',
            padding: '10px 20px',
            background: 'var(--color-accent)',
            color: 'var(--color-bg-primary)',
            borderRadius: 'var(--radius-md)',
            fontWeight: '600'
          }}
        >
          Retry Connection
        </button>
      </div>
    );
  }

  const {
    profile,
    skill_categories,
    experiences,
    projects,
    education,
    leadership,
    awards,
  } = data || {};

  return (
    <>
      <Navbar />
      <Hero profile={profile} />
      <About profile={profile} />
      <Skills skillCategories={skill_categories} />
      <Experience experiences={experiences} />
      <Projects projects={projects} />
      <Education education={education} />
      <Leadership leadership={leadership} />
      <Awards awards={awards} />
      <Contact profile={profile} />
      <Footer profile={profile} />
    </>
  );
}
