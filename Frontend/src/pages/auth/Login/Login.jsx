import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import api from "../../../services/api";
import "./Login.css";

const Login = () => {
  const navigate = useNavigate();

  // -----------------------------
  // State
  // -----------------------------
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  const [errors, setErrors] = useState({
    email: "",
    password: "",
  });

  // -----------------------------
  // Validation
  // -----------------------------
  const validateForm = () => {
    const newErrors = {
      email: "",
      password: "",
    };

    let isValid = true;

    const trimmedEmail = email.trim();

    // Email Validation
    if (!trimmedEmail) {
      newErrors.email = "Email address is required.";
      isValid = false;
    } else if (
      !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(trimmedEmail)
    ) {
      newErrors.email = "Please enter a valid email address.";
      isValid = false;
    }

    // Password Validation
    if (!password) {
      newErrors.password = "Password is required.";
      isValid = false;
    } else if (password.length < 8) {
      newErrors.password =
        "Password must be at least 8 characters long.";
      isValid = false;
    }

    setErrors(newErrors);
    return isValid;
  };

  // -----------------------------
  // Submit Handler
  // -----------------------------
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    setLoading(true);

    try {
      const response = await api.post("/login", {
        email: email.trim(),
        password,
      });

      // -----------------------------
      // Clear Previous Authentication
      // -----------------------------
      localStorage.removeItem("token");
      localStorage.removeItem("user");

      sessionStorage.removeItem("token");
      sessionStorage.removeItem("user");

      // -----------------------------
      // Store Authentication
      // -----------------------------
      if (rememberMe) {
        localStorage.setItem("token", response.data.token);
        localStorage.setItem(
          "user",
          JSON.stringify(response.data.user)
        );
      } else {
        sessionStorage.setItem("token", response.data.token);
        sessionStorage.setItem(
          "user",
          JSON.stringify(response.data.user)
        );
      }

      console.log("Login Successful");

      // Clear Form
      setEmail("");
      setPassword("");

      // -----------------------------
      // Redirect According To Role
      // -----------------------------
      if (response.data.user.role === "GOVERNMENT_ADMIN") {
        navigate("/government/dashboard");
      } else {
        navigate("/citizen/dashboard");
      }

    } catch (error) {
      console.error("Login Error:", error);

      alert(
        error.response?.data?.message ||
        "Unable to connect to the server."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">

        <h1>Welcome Back</h1>

        <p>
          Sign in to continue to Policy Intelligence Platform
        </p>

        <form onSubmit={handleSubmit} noValidate>

          {/* Email */}

          <div className="form-group">

            <label>Email Address</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);

                if (errors.email) {
                  setErrors({
                    ...errors,
                    email: "",
                  });
                }
              }}
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
                type={showPassword ? "text" : "password"}
                placeholder="Enter your password"
                value={password}
                onChange={(e) => {
                  setPassword(e.target.value);

                  if (errors.password) {
                    setErrors({
                      ...errors,
                      password: "",
                    });
                  }
                }}
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

          {/* Options */}

          <div className="login-options">

            <label className="remember-me">

              <input
                type="checkbox"
                checked={rememberMe}
                onChange={() =>
                  setRememberMe(!rememberMe)
                }
              />

              Remember Me

            </label>

            <button
              type="button"
              className="forgot-password"
              onClick={() =>
                alert(
                  "Forgot Password feature will be added later."
                )
              }
            >
              Forgot Password?
            </button>

          </div>

          {/* Login Button */}

          <button
            type="submit"
            className="login-btn"
            disabled={loading}
          >
            {loading ? "Logging in..." : "Login"}
          </button>

        </form>

        <div className="register-link">

          Don't have an account?{" "}

          <span onClick={() => navigate("/register")}>
            Register
          </span>

        </div>

      </div>
    </div>
  );
};

export default Login;