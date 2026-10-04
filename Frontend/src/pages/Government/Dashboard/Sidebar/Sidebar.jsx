import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  ClipboardList,
  ScrollText,
  Scale,
  Newspaper,
  BarChart3,
  User,
} from "lucide-react";

import "./Sidebar.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">

      <div className="sidebar-logo">
        <h2>PolicyLens</h2>
        <span>Government Admin</span>
      </div>

      <nav className="sidebar-menu">

        <NavLink to="/government/dashboard" className="menu-item">
          <LayoutDashboard size={20} />
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/government/review-queue" className="menu-item">
          <ClipboardList size={20} />
          <span>Review Queue</span>
        </NavLink>

        <NavLink to="/government/policy-explorer" className="menu-item">
          <ScrollText size={20} />
          <span>Policy Management</span>
        </NavLink>

        <NavLink to="/government/clause-insights" className="menu-item">
          <Scale size={20} />
          <span>Clause Insights</span>
        </NavLink>

        <NavLink to="/government/media-analysis" className="menu-item">
          <Newspaper size={20} />
          <span>Media Analysis</span>
        </NavLink>

        <NavLink to="/government/analytics" className="menu-item">
          <BarChart3 size={20} />
          <span>Analytics</span>
        </NavLink>

        <div className="menu-divider"></div>

        <NavLink to="/government/profile" className="menu-item">
          <User size={20} />
          <span>Profile</span>
        </NavLink>

      </nav>

    </aside>
  );
};

export default Sidebar;