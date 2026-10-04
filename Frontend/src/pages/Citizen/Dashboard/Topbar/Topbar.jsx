import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
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

            <div className="topbar-right">

                <div
                    className="profile"
                    onClick={() => navigate("/citizen/profile")}
                    title="View Profile"
                >

                    <div className="avatar">

                        {user?.full_name?.charAt(0).toUpperCase() || "U"}

                    </div>

                    <div className="profile-info">

                        <h4>
                            {user?.full_name || "User"}
                        </h4>

                        <span>
                            {user?.role === "GOVERNMENT"
                                ? "Government"
                                : "Citizen"}
                        </span>

                    </div>

                </div>

            </div>

        </header>

    );

};

export default Topbar;