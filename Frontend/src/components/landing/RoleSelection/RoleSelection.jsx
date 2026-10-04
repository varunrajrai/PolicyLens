import "./RoleSelection.css";
import { FaUser, FaUniversity } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

function RoleSelection() {

  const navigate = useNavigate();

  return (
    <section className="roles">

      <div className="roles-heading">

        <h2>Choose Your Portal</h2>

        <p>
          PolicyLens provides dedicated interfaces for citizens and
          government administrators, ensuring secure access and
          personalized workflows.
        </p>

      </div>

      <div className="roles-container">

        {/* Citizen Portal */}

        <div className="role-card citizen">

          <FaUser className="role-icon" />

          <h3>Citizen Portal</h3>

          <ul>

            <li>Submit policy feedback</li>

            <li>Track submission status</li>

            <li>View clause mapping</li>

            <li>Receive policy updates</li>

          </ul>

          <button
            onClick={() => navigate("/login")}
          >
            Login as Citizen
          </button>

        </div>

        {/* Government Portal */}

        <div className="role-card government">

          <FaUniversity className="role-icon" />

          <h3>Government Portal</h3>

          <ul>

            <li>Review policy analytics</li>

            <li>Manage citizen feedback</li>

            <li>View clause-wise analysis</li>

            <li>Access AI recommendations</li>

          </ul>

          <button
            onClick={() => navigate("/login")}
          >
            Login as Government
          </button>

        </div>

      </div>

    </section>
  );
}

export default RoleSelection;