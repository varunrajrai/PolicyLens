import { Navigate } from "react-router-dom";

const AdminRoute = ({ children }) => {
  const token =
    localStorage.getItem("token") ||
    sessionStorage.getItem("token");

  const user =
    JSON.parse(localStorage.getItem("user")) ||
    JSON.parse(sessionStorage.getItem("user"));

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  if (user.role !== "government_admin") {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
};

export default AdminRoute;