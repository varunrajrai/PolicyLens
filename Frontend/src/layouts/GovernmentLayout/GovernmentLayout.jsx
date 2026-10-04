import { Outlet } from "react-router-dom";

import Sidebar from "../../pages/Government/Dashboard/Sidebar/Sidebar";
import Topbar from "../../pages/Government/Dashboard/Topbar/Topbar";

import "./GovernmentLayout.css";

const GovernmentLayout = () => {
  return (
    <div className="dashboard-layout">

      <Sidebar />

      <div className="dashboard-main">

        <Topbar />

        <div className="dashboard-content">
          <Outlet />
        </div>

      </div>

    </div>
  );
};

export default GovernmentLayout;