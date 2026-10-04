import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import { ShieldCheck } from "lucide-react";

import "./Topbar.css";

const Topbar = () => {
    const navigate = useNavigate();

    const user = useMemo(() => {
        const storedUser =
            localStorage.getItem("user") ||
            sessionStorage.getItem("user");

        return storedUser ? JSON.parse(storedUser) : null;
    }, []);

    return (
        <header className="topbar">

            {/* Left Section */}

            <div className="topbar-left">

                <h2>Government Dashboard</h2>

                <p>Policy Intelligence & Monitoring System</p>

            </div>

            {/* Right Section */}

            <div className="topbar-right">

                <div
                    className="profile"
                    onClick={() => navigate("/government/profile")}
                    title="View Profile"
                >

                    <div className="avatar">
                        {user?.full_name?.charAt(0).toUpperCase() || "G"}
                    </div>

                    <div className="profile-info">

                        <h4>{user?.full_name || "Government Admin"}</h4>

                        <span>
                            <ShieldCheck size={14} />
                            Government Admin
                        </span>

                    </div>

                </div>

            </div>

        </header>
    );
};

export default Topbar;