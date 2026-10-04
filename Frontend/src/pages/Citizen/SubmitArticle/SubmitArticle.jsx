import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../../services/api";
import "./SubmitArticle.css";

const SubmitArticle = () => {

  const navigate = useNavigate();

  const [loading, setLoading] = useState(false);

  const [form, setForm] = useState({
    title: "",
    source: "",
    amendment: "",
    url: "",
    article: "",
  });

  const wordCount = form.article.trim()
    ? form.article.trim().split(/\s+/).length
    : 0;

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const submit = async (e) => {

    e.preventDefault();

    if (
      !form.title ||
      !form.source ||
      !form.amendment ||
      !form.article
    ) {
      alert("Please fill in all required fields.");
      return;
    }

    setLoading(true);

    try {

      await api.post("/citizen/articles", form);

      alert("Article submitted successfully!");

      setForm({
        title: "",
        source: "",
        amendment: "",
        url: "",
        article: "",
      });

      navigate("/citizen/my-articles");

    } catch (error) {

      console.error(error);

      alert(
        error.response?.data?.message ||
        "Failed to submit article."
      );

    } finally {

      setLoading(false);

    }

  };

  return (
    <div className="submit-page">

      <div className="submit-header">

        <h1>Submit Policy Article</h1>

        <p>
          Paste a policy-related article for AI-powered legislative
          analysis and government review.
        </p>

      </div>

      <form
        className="submit-card"
        onSubmit={submit}
      >

        <div className="form-group">

          <label>Article Title *</label>

          <input
            type="text"
            name="title"
            placeholder="Enter article title"
            value={form.title}
            onChange={handleChange}
          />

        </div>

        <div className="row">

          <div className="form-group">

            <label>Source *</label>

            <input
              type="text"
              name="source"
              placeholder="e.g. The Hindu"
              value={form.source}
              onChange={handleChange}
            />

          </div>

          <div className="form-group">

            <label>Amendment *</label>

            <select
              name="amendment"
              value={form.amendment}
              onChange={handleChange}
            >
              <option value="">
                Select Amendment
              </option>

              <option value="CAA">
                CAA
              </option>

              <option value="NRC">
                NRC
              </option>

              <option value="CAA + NRC">
                CAA + NRC
              </option>

            </select>

          </div>

        </div>

        <div className="form-group">

          <label>
            Original Article URL (Optional)
          </label>

          <input
            type="url"
            name="url"
            placeholder="https://example.com"
            value={form.url}
            onChange={handleChange}
          />

        </div>

        <div className="form-group">

          <div className="article-header">

            <label>
              Paste Complete Article *
            </label>

            <span>
              {wordCount} words
            </span>

          </div>

          <textarea
            rows="16"
            name="article"
            placeholder="Paste the complete article here..."
            value={form.article}
            onChange={handleChange}
          />

        </div>

        <div className="info-box">

          <h4>Submission Guidelines</h4>

          <ul>

            <li>
              Paste the complete article text.
            </li>

            <li>
              Mention the original source whenever possible.
            </li>

            <li>
              Select the correct amendment category.
            </li>

            <li>
              Your article will automatically enter the AI analysis pipeline.
            </li>

          </ul>

        </div>

        <div className="actions">

          <button
            type="button"
            className="cancel-btn"
            onClick={() =>
              navigate("/citizen/dashboard")
            }
          >
            Cancel
          </button>

          <button
            type="submit"
            className="submit-btn"
            disabled={loading}
          >
            {loading
              ? "Submitting..."
              : "Submit Article →"}
          </button>

        </div>

      </form>

    </div>
  );
};

export default SubmitArticle;