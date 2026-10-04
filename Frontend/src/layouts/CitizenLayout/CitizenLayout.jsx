import { Outlet } from "react-router-dom";

import Sidebar from "../../pages/Citizen/Dashboard/Sidebar/Sidebar";
import Topbar from "../../pages/Citizen/Dashboard/Topbar/Topbar";

import "./CitizenLayout.css";

const DashboardLayout = () => {
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

export default DashboardLayout;