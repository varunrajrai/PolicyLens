import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../../services/api";
import "./Dashboard.css";

const Dashboard = () => {
  const navigate = useNavigate();

  const [loading, setLoading] = useState(true);

  const [dashboard, setDashboard] = useState({
    user_name: "",
    articles_submitted: 0,
    under_review: 0,
    priority_selected: 0,
    used_in_reports: 0,
    recent_articles: [],
  });

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const response = await api.get("/citizen/dashboard");
      setDashboard(response.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (date) =>
    new Date(date).toLocaleDateString("en-IN", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    });

  const truncate = (text, len = 65) =>
    text.length > len ? text.substring(0, len) + "..." : text;

  if (loading) return <h2>Loading Dashboard...</h2>;

  const stats = [
    { title: "Articles Submitted", value: dashboard.articles_submitted },
    { title: "Under Review", value: dashboard.under_review },
    { title: "Priority Selected", value: dashboard.priority_selected },
    { title: "Used In Reports", value: dashboard.used_in_reports },
  ];

  return (
    <div className="citizen-dashboard">
      <section className="dashboard-header">
        <div className="header-content">
          <h1>Welcome Back, {dashboard.user_name} 👋</h1>
          <p>Track your submitted policy articles and government feedback.</p>
        </div>

        <button
          className="submit-btn"
          onClick={() => navigate("/citizen/submit-article")}
        >
          + Submit Article
        </button>
      </section>

      <section className="stats">
        {stats.map((item) => (
          <div className="stat-card" key={item.title}>
            <h4>{item.title}</h4>
            <h2>{item.value}</h2>
          </div>
        ))}
      </section>

      <section className="recent-card">
        <div className="recent-header">
          <h3>Recent Articles</h3>

          <button onClick={() => navigate("/citizen/my-articles")}>
            View All
          </button>
        </div>

        <table>
          <thead>
            <tr>
              <th>Article</th>
              <th>Status</th>
              <th>Submitted</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            {dashboard.recent_articles.length === 0 ? (
              <tr>
                <td colSpan="4" style={{ textAlign: "center" }}>
                  No articles submitted yet.
                </td>
              </tr>
            ) : (
              dashboard.recent_articles.map((article) => (
                <tr key={article.article_id}>
                  <td>{truncate(article.title)}</td>

                  <td>
                    <span
                      className={`status ${article.status.toLowerCase()}`}
                    >
                      {article.status}
                    </span>
                  </td>

                  <td>{formatDate(article.submission_date)}</td>

                  <td>
                    <button
                      className="view-btn"
                      onClick={() =>
                        navigate(`/citizen/policy-review/${article.article_id}`)
                      }
                    >
                      View
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </section>
    </div>
  );
};

export default Dashboard;
