import "./Hero.css";
import { useNavigate } from "react-router-dom";

function Hero() {

  const navigate = useNavigate();

  return (
    <section className="hero">

      {/* Left Side */}

      <div className="hero-left">

        <span className="hero-badge">
          NLP-Powered Legislative Intelligence
        </span>

        <h1>
          Understand Public Opinion
          <span> Before Policies Become Law</span>
        </h1>

        <p>
          PolicyLens leverages Natural Language Processing and Machine
          Learning to analyze legislative amendments, map citizen
          feedback to individual clauses, detect public sentiment,
          prioritize meaningful responses, and generate actionable
          insights for policymakers.
        </p>

        <div className="hero-buttons">

          <button
            className="primary-btn"
            onClick={() => navigate("/login")}
          >
            Citizen Login
          </button>

          <button
            className="secondary-btn"
            onClick={() => navigate("/login")}
          >
            Government Login
          </button>

        </div>

        <small>
          Role-Based Access • Secure Authentication • AI Powered
        </small>

      </div>

      {/* Right Side */}

      <div className="hero-right">

        <div className="dashboard">

          <div className="dashboard-header">

            <h3>Government Dashboard</h3>

            <span>Preview</span>

          </div>

          <div className="summary-grid">

            <div className="summary-card">
              <h2>3+</h2>
              <p>Amendments</p>
            </div>

            <div className="summary-card">
              <h2>50+</h2>
              <p>Citizen Responses</p>
            </div>

            <div className="summary-card">
              <h2>120+</h2>
              <p>Policy Clauses</p>
            </div>

            <div className="summary-card">
              <h2>4</h2>
              <p>AI Models</p>
            </div>

          </div>

        </div>

      </div>

    </section>
  );
}

export default Hero;