import "./Navbar.css";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">

      {/* Logo */}

      <Link
        to="/"
        className="navbar-logo"
      >
        PolicyLens
      </Link>

      {/* Navigation */}

      <ul className="navbar-links">

        <li className="navbar-item">
          <Link
            to="/"
            className="navbar-link"
          >
            Home
          </Link>
        </li>

        <li className="navbar-item">
          <Link
            to="/"
            className="navbar-link"
          >
            Features
          </Link>
        </li>

        <li className="navbar-item">
          <Link
            to="/"
            className="navbar-link"
          >
            About
          </Link>
        </li>

        <li className="navbar-item">
          <Link
            to="/"
            className="navbar-link"
          >
            Contact
          </Link>
        </li>

      </ul>

      {/* Authentication */}

      <div className="navbar-auth">

        <Link
          to="/login"
          className="navbar-login-btn"
        >
          Login
        </Link>

        <Link
          to="/register"
          className="navbar-register-btn"
        >
          Register
        </Link>

      </div>

    </nav>
  );
}

export default Navbar;