import "./Profile.css";

const Profile = () => {
  return (
    <div className="profile-page">

      <div className="profile-header">

        <div className="profile-avatar">
          V
        </div>

        <div>

          <h1>Varun Raj Rai</h1>

          <p>Citizen • PolicyLens Member</p>

        </div>

      </div>

      <div className="profile-grid">

        <div className="profile-card">

          <h2>Personal Information</h2>

          <div className="info-group">
            <label>Full Name</label>
            <input value="Varun Raj Rai" readOnly />
          </div>

          <div className="info-group">
            <label>Email</label>
            <input value="varun@example.com" readOnly />
          </div>

          <div className="info-group">
            <label>Role</label>
            <input value="Citizen" readOnly />
          </div>

        </div>

        <div className="profile-card">

          <h2>Account Statistics</h2>

          <div className="stat">
            <span>Articles Submitted</span>
            <strong>12</strong>
          </div>

          <div className="stat">
            <span>Articles Selected</span>
            <strong>2</strong>
          </div>

          <div className="stat">
            <span>Under Review</span>
            <strong>3</strong>
          </div>

          <div className="stat">
            <span>Member Since</span>
            <strong>July 2026</strong>
          </div>

        </div>

      </div>

      <div className="profile-card">

        <h2>Account Actions</h2>

        <div className="action-buttons">

          <button>Edit Profile</button>

          <button className="secondary">
            Change Password
          </button>

          <button className="danger">
            Logout
          </button>

        </div>

      </div>

    </div>
  );
};

export default Profile;