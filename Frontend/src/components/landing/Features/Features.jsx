import "./Features.css";

import {
  FaPuzzlePiece,
  FaChartLine,
  FaBalanceScale,
  FaComments,
  FaFileAlt,
  FaUserShield,
} from "react-icons/fa";

const features = [
  {
    id: 1,
    icon: <FaPuzzlePiece />,
    title: "Clause Mapping",
    description:
      "Uses Sentence Transformer embeddings to automatically associate citizen feedback with the most relevant legislative clauses.",
  },
  {
    id: 2,
    icon: <FaChartLine />,
    title: "Priority Analysis",
    description:
      "Ranks responses using multiple evaluation metrics, helping policymakers focus on the most impactful public concerns first.",
  },
  {
    id: 3,
    icon: <FaBalanceScale />,
    title: "Public Stance Detection",
    description:
      "Classifies each response as Support, Oppose or Neutral using transformer-based zero-shot classification models.",
  },
  {
    id: 4,
    icon: <FaComments />,
    title: "Clause-wise Debate",
    description:
      "Groups supporting and opposing viewpoints into structured debates for every legislative clause.",
  },
  {
    id: 5,
    icon: <FaFileAlt />,
    title: "Intelligent Summarization",
    description:
      "Generates concise summaries of thousands of citizen responses, enabling faster policy review.",
  },
  {
    id: 6,
    icon: <FaUserShield />,
    title: "Role-Based Platform",
    description:
      "Separate portals for citizens and government officials ensure secure access and personalized workflows.",
  },
];

function Features() {
  return (
    <section className="features">

      <div className="features-heading">

        <h2>Why PolicyLens?</h2>

        <p>
          Built to simplify legislative analysis through modern Natural
          Language Processing, making policy review faster, transparent and
          data-driven.
        </p>

      </div>

      <div className="features-grid">

        {features.map((feature) => (

          <div key={feature.id} className="feature-card">

            <div className="feature-icon">

              {feature.icon}

            </div>

            <h3>{feature.title}</h3>

            <p>{feature.description}</p>

          </div>

        ))}

      </div>

    </section>
  );
}

export default Features;