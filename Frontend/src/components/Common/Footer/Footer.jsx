import "./Footer.css";
import { FaGithub, FaLinkedin, FaEnvelope } from "react-icons/fa";

function Footer() {
  return (
    <footer className="footer">

      <div className="footer-brand">

        <h2>Policy<span>Lens</span></h2>

        <p>
          Transforming Citizen Feedback into Better Policy Decisions.
        </p>

      </div>

      <div className="footer-grid">

        <div>

          <h4>Product</h4>

          <a href="#">Home</a>
          <a href="#">Pipeline</a>
          <a href="#">Features</a>

        </div>

        <div>

          <h4>Portals</h4>

          <a href="#">Citizen Portal</a>
          <a href="#">Government Portal</a>
          <a href="#">Register</a>

        </div>

        <div>

          <h4>Resources</h4>

          <a href="#">About</a>
          <a href="#">Documentation</a>
          <a href="#">GitHub</a>

        </div>

        <div>

          <h4>Contact</h4>

          <a href="#"><FaEnvelope /> Email</a>
          <a href="#"><FaLinkedin /> LinkedIn</a>
          <a href="#"><FaGithub /> GitHub</a>

        </div>

      </div>

      <div className="footer-bottom">

        © 2026 PolicyLens. All Rights Reserved.

      </div>

    </footer>
  );
}

export default Footer;