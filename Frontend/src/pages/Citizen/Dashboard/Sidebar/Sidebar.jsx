import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  FilePlus2,
  Files,
  ClipboardCheck,
  User,
} from "lucide-react";

import "./Sidebar.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">

      {/* Logo */}

      <div className="sidebar-logo">
        <h2>PolicyLens</h2>
        <span>Citizen Portal</span>
      </div>

      {/* Navigation */}

      <nav className="sidebar-menu">

        <NavLink to="/citizen/dashboard" className="menu-item">
          <LayoutDashboard size={20} />
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/citizen/submit-article" className="menu-item">
          <FilePlus2 size={20} />
          <span>Submit Article</span>
        </NavLink>

        <NavLink to="/citizen/my-articles" className="menu-item">
          <Files size={20} />
          <span>My Articles</span>
        </NavLink>

        <NavLink to="/citizen/policy-review" className="menu-item">
          <ClipboardCheck size={20} />
          <span>Policy Review</span>
        </NavLink>

        <div className="menu-divider"></div>

        <NavLink to="/citizen/profile" className="menu-item">
          <User size={20} />
          <span>Profile</span>
        </NavLink>

      </nav>

    </aside>
  );
};

export default Sidebar;