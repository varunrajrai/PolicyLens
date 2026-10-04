import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../../services/api";
import "./MyArticles.css";

export default function MyArticles() {

  const navigate = useNavigate();

  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("ALL");

  useEffect(() => {
    fetchArticles();
  }, []);

  const fetchArticles = async () => {

    try {

      const response = await api.get("/citizen/articles");

      setArticles(response.data);

    } catch (err) {

      console.error(err);

    } finally {

      setLoading(false);

    }

  };

  const filteredArticles = useMemo(() => {

    return articles.filter((article) => {

      const searchMatch = article.title
        .toLowerCase()
        .includes(search.toLowerCase());

      const statusMatch =
        status === "ALL" ||
        article.status === status;

      return searchMatch && statusMatch;

    });

  }, [articles, search, status]);

  if (loading) {

    return (
      <div className="myArticles">
        <h2>Loading Articles...</h2>
      </div>
    );

  }

  return (

    <div className="myArticles">

      <div className="hero-article">

        <h1>My Articles</h1>

        <p>
          Manage all policy articles submitted for AI-powered legislative analysis.
        </p>

      </div>

      <div className="toolbar">

        <input
          type="text"
          placeholder="Search articles..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >

          <option value="ALL">All Status</option>
          <option value="PENDING">Pending</option>
          <option value="PROCESSING">Processing</option>
          <option value="REVIEWED">Reviewed</option>

        </select>

      </div>

      <p className="count">

        {filteredArticles.length} Articles Found

      </p>

      {filteredArticles.length === 0 ? (

        <div className="empty">

          <h2>No Articles Found</h2>

          <p>
            Submit your first article to begin AI analysis.
          </p>

          <button
            onClick={() => navigate("/citizen/submit")}
          >
            Submit Article
          </button>

        </div>

      ) : (

        <div className="grid">

          {filteredArticles.map((article) => (

            <div
              className="card"
              key={article.article_id}
            >

              <div className="cardTop">

                <div>

                  <span className="tag">
                    {article.amendment}
                  </span>

                  <h2>
                    {article.title}
                  </h2>

                </div>

                <span
                  className={`badge ${article.status.toLowerCase()}`}
                >
                  {article.status}
                </span>

              </div>

              <div className="details">

                <div>

                  <strong>Source</strong>

                  <p>{article.source}</p>

                </div>

                <div>

                  <strong>Submitted</strong>

                  <p>
                    {new Date(article.submission_date).toLocaleDateString()}
                  </p>

                </div>

                <div>

                  <strong>Current Stage</strong>

                  <p>{article.current_stage}</p>

                </div>

              </div>

              <button
                className="viewBtn"
                onClick={() =>
                  navigate(`/citizen/policy-review/${article.article_id}`)
                }
              >

                View Analysis →

              </button>

            </div>

          ))}

        </div>

      )}

    </div>

  );

}