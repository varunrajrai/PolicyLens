import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../../../services/api";
import "./PolicyReview.css";


export default function PolicyReview() {
    
    const navigate = useNavigate();
    const { articleId } = useParams();
    if (!articleId) {
return (

    <div className="policyEmpty">

        <div className="emptyCard">

            <div className="emptyIcon">
                ⚠️
            </div>

            <h1>Policy Review Unavailable</h1>

            <p>

                The requested article could not be found or you do not
                have permission to access it.

            </p>

            <button
    className="backBtn"
    onClick={() => {
        console.log("Button clicked");
        navigate("/citizen/my-articles");
    }}
>
    ← Back to My Articles
</button>
        </div>

    </div>

);
    }

    const [review, setReview] = useState(null);
    const [loading, setLoading] = useState(true);
    const [showArticle, setShowArticle] = useState(false);

    useEffect(() => {
        fetchReview();
    }, [articleId]);

    const fetchReview = async () => {

        try {

            const response = await api.get(
                `/citizen/articles/${articleId}/review`
            );

            if (response.data.success) {
                setReview(response.data.data);
            } else {
                setReview(null);
            }

        } catch (err) {

            console.error(err);
            setReview(null);

        } finally {

            setLoading(false);

        }

    };

    if (loading) {
        return (
            <div className="policy-loading">
                <h2>Loading Policy Analysis...</h2>
            </div>
        );
    }

    if (!review) {
        return (
            <div className="policy-loading">
                <h2>Unable to load article.</h2>

                <button
                    className="backBtn"
                    onClick={() => navigate("/citizen/my-articles")}
                >
                    Back
                </button>

            </div>
        );
    }

    const {
        article,
        summary,
        statistics,
        clauses,
        stance_distribution,
        analysis_status
    } = review;

    const total =
        stance_distribution["Pro-CAA/NRC"] +
        stance_distribution["Neutral"] +
        stance_distribution["Anti-CAA/NRC"];

    const percent = (count) => {

        if (total === 0) return 0;

        return Math.round((count / total) * 100);

    };

    return (

        <div className="policyPage">

            <button
                className="backBtn"
                onClick={() => navigate("/citizen/my-articles")}
            >
                ← Back to My Articles
            </button>

            <div className="headerCard">

                <h1>{article.title}</h1>

                <div className="meta">

                    <span>{article.source}</span>

                    <span>{article.amendment}</span>

                    <span>{article.status}</span>

                    <span>
                        {new Date(
                            article.submission_date
                        ).toLocaleDateString()}
                    </span>

                </div>

            </div>

            <div className="summaryCard">

                <h2>AI Generated Summary</h2>

                <p>{summary}</p>

            </div>

            <h2 className="sectionTitle">
                AI Analysis Overview
            </h2>

            <div className="statsGrid">

                <div className="statCard">

                    <h3>Overall Stance</h3>

                    <h1> <div classname="stances">{statistics.overall_stance}</div></h1>

                </div>

                <div className="statCard">

                    <h3>Paragraphs</h3>

                    <h1>{statistics.paragraphs}</h1>

                </div>

                <div className="statCard">

                    <h3>Detected Clauses</h3>

                    <h1>{statistics.detected_clauses}</h1>

                </div>

                <div className="statCard">

                    <h3>High Priority</h3>

                    <h1>{statistics.high_priority}</h1>

                </div>

                <div className="statCard">

                    <h3>Average Priority</h3>

                    <h1>{statistics.average_priority}</h1>

                </div>

                <div className="statCard">

                    <h3>Confidence</h3>

                    <h1>{statistics.average_confidence}%</h1>

                </div>

            </div>

            <div className="analysisGrid">

                <div className="stanceCard">

                    <h2>Stance Distribution</h2>

                    {!analysis_status.stance_available ? (

                        <div className="noAnalysis">

                            <p>

                                Stance analysis is not available
                                for this article.

                            </p>

                        </div>

                    ) : (

                        <>

                            <div className="stanceRow">

                                <span>Pro</span>

                                <div className="bar">

                                    <div
                                        className="fill pro"
                                        style={{
                                            width:
                                                percent(
                                                    stance_distribution["Pro-CAA/NRC"]
                                                ) + "%"
                                        }}
                                    />

                                </div>

                                <span>

                                    {stance_distribution["Pro-CAA/NRC"]}

                                    {" ("}

                                    {percent(
                                        stance_distribution["Pro-CAA/NRC"]
                                    )}

                                    %)

                                </span>

                            </div>

                            <div className="stanceRow">

                                <span>Neutral</span>

                                <div className="bar">

                                    <div
                                        className="fill neutral"
                                        style={{
                                            width:
                                                percent(
                                                    stance_distribution["Neutral"]
                                                ) + "%"
                                        }}
                                    />

                                </div>

                                <span>

                                    {stance_distribution["Neutral"]}

                                    {" ("}

                                    {percent(
                                        stance_distribution["Neutral"]
                                    )}

                                    %)

                                </span>

                            </div>

                            <div className="stanceRow">

                                <span>Anti</span>

                                <div className="bar">

                                    <div
                                        className="fill anti"
                                        style={{
                                            width:
                                                percent(
                                                    stance_distribution["Anti-CAA/NRC"]
                                                ) + "%"
                                        }}
                                    />

                                </div>

                                <span>

                                    {stance_distribution["Anti-CAA/NRC"]}

                                    {" ("}

                                    {percent(
                                        stance_distribution["Anti-CAA/NRC"]
                                    )}

                                    %)

                                </span>

                            </div>

                        </>

                    )}

                </div>

                <div className="clauseCard">

                    <h2>Clause Coverage</h2>

                    <table>

                        <thead>

                            <tr>

                                <th>Clause</th>
                                <th>Paragraphs</th>
                                <th>Similarity</th>

                            </tr>

                        </thead>

                        <tbody>

                            {clauses.map((clause, index) => (

                                <tr key={index}>

                                    <td>{clause.clause_name}</td>

                                    <td>{clause.paragraph_count}</td>

                                    <td>{clause.average_similarity}%</td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </div>

            <div className="articleCard">

                <div className="articleTop">

                    <h2>Original Article</h2>

                    <button
                        onClick={() =>
                            setShowArticle(!showArticle)
                        }
                    >
                        {showArticle
                            ? "Hide Article"
                            : "Show Article"}
                    </button>

                </div>

                {showArticle && (

                    <div className="articleText">

                        {article.article_text}

                    </div>

                )}

            </div>

        </div>

    );

}