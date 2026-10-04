import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import api from "../../../services/api";
import "./Register.css";

const Register = () => {
  const navigate = useNavigate();

  // -----------------------------
  // State
  // -----------------------------
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("citizen");

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] =
    useState(false);

  const [loading, setLoading] = useState(false);

  const [errors, setErrors] = useState({
    fullName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  // -----------------------------
  // Validation
  // -----------------------------
  const validateForm = () => {
    const newErrors = {
      fullName: "",
      email: "",
      password: "",
      confirmPassword: "",
    };

    let isValid = true;

    if (!fullName.trim()) {
      newErrors.fullName = "Full name is required.";
      isValid = false;
    }

    if (!email.trim()) {
      newErrors.email = "Email address is required.";
      isValid = false;
    } else if (
      !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(email)
    ) {
      newErrors.email = "Please enter a valid email.";
      isValid = false;
    }

    if (!password) {
      newErrors.password = "Password is required.";
      isValid = false;
    } else if (password.length < 8) {
      newErrors.password =
        "Password must be at least 8 characters.";
      isValid = false;
    }

    if (!confirmPassword) {
      newErrors.confirmPassword =
        "Please confirm your password.";
      isValid = false;
    } else if (password !== confirmPassword) {
      newErrors.confirmPassword =
        "Passwords do not match.";
      isValid = false;
    }

    setErrors(newErrors);

    return isValid;
  };

  // -----------------------------
  // Submit
  // -----------------------------
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    setLoading(true);

    try {
      const response = await api.post("/signup", {
        full_name: fullName.trim(),
        email: email.trim(),
        password,
        role,
      });

      alert(response.data.message);

      navigate("/login");

    } catch (error) {

      alert(
        error.response?.data?.message ||
          "Registration failed."
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="login-page">

      <div className="login-card">

        <h1>Create Account</h1>

        <p>
          Join the Policy Intelligence Platform
        </p>

        <form onSubmit={handleSubmit} noValidate>

          {/* Full Name */}

          <div className="form-group">

            <label>Full Name</label>

            <input
              type="text"
              placeholder="Enter your full name"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
            />

            {errors.fullName && (
              <small className="error-text">
                {errors.fullName}
              </small>
            )}

          </div>

          {/* Email */}

          <div className="form-group">

            <label>Email</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            {errors.email && (
              <small className="error-text">
                {errors.email}
              </small>
            )}

          </div>

          {/* Password */}

          <div className="form-group">

            <label>Password</label>

            <div className="password-field">

              <input
                type={
                  showPassword ? "text" : "password"
                }
                placeholder="Enter password"
                value={password}
                onChange={(e) =>
                  setPassword(e.target.value)
                }
              />

              <button
                type="button"
                className="toggle-password"
                onClick={() =>
                  setShowPassword(!showPassword)
                }
              >
                {showPassword ? (
                  <FaEyeSlash />
                ) : (
                  <FaEye />
                )}
              </button>

            </div>

            {errors.password && (
              <small className="error-text">
                {errors.password}
              </small>
            )}

          </div>

          {/* Confirm Password */}

          <div className="form-group">

            <label>Confirm Password</label>

            <div className="password-field">

              <input
                type={
                  showConfirmPassword
                    ? "text"
                    : "password"
                }
                placeholder="Confirm password"
                value={confirmPassword}
                onChange={(e) =>
                  setConfirmPassword(
                    e.target.value
                  )
                }
              />

              <button
                type="button"
                className="toggle-password"
                onClick={() =>
                  setShowConfirmPassword(
                    !showConfirmPassword
                  )
                }
              >
                {showConfirmPassword ? (
                  <FaEyeSlash />
                ) : (
                  <FaEye />
                )}
              </button>

            </div>

            {errors.confirmPassword && (
              <small className="error-text">
                {errors.confirmPassword}
              </small>
            )}

          </div>

          {/* Role */}

          <div className="form-group">

            <label>Select Role</label>

            <select
              value={role}
              onChange={(e) =>
                setRole(e.target.value)
              }
            >
              <option value="citizen">
                Citizen
              </option>

              <option value="government_admin">
                Government Admin
              </option>

            </select>

          </div>

          <button
            className="login-btn"
            type="submit"
            disabled={loading}
          >
            {loading
              ? "Creating Account..."
              : "Register"}
          </button>

        </form>

        <div className="register-link">

          Already have an account?{" "}

          <span
            onClick={() =>
              navigate("/login")
            }
          >
            Login
          </span>

        </div>

      </div>

    </div>
  );
};

export default Register;