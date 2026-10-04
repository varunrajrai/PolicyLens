import "./Pipeline.css";

import {
  FaUsers,
  FaPuzzlePiece,
  FaChartLine,
  FaBalanceScale,
  FaComments,
  FaFileAlt,
  FaUniversity,
  FaGavel,
} from "react-icons/fa";

const pipelineSteps = [
  {
    id: 1,
    icon: <FaUsers />,
    title: "Citizen Feedback",
    subtitle: "Stage 01",
    description:
      "Citizens submit opinions, articles and feedback regarding a proposed amendment.",
    color: "#10B981",
  },
  {
    id: 2,
    icon: <FaPuzzlePiece />,
    title: "Clause Mapping",
    subtitle: "Stage 02",
    description:
      "Semantic embeddings map every response to the most relevant amendment clauses.",
    color: "#6366F1",
  },
  {
    id: 3,
    icon: <FaChartLine />,
    title: "Priority Scoring",
    subtitle: "Stage 03",
    description:
      "Machine learning ranks responses based on importance and relevance.",
    color: "#F59E0B",
  },
  {
    id: 4,
    icon: <FaBalanceScale />,
    title: "Stance Detection",
    subtitle: "Stage 04",
    description:
      "Responses are classified into Support, Oppose or Neutral categories.",
    color: "#8B5CF6",
  },
  {
    id: 5,
    icon: <FaComments />,
    title: "Clause-wise Debate",
    subtitle: "Stage 05",
    description:
      "Arguments from different viewpoints are organized clause by clause.",
    color: "#06B6D4",
  },
  
  {
    id: 6,
    icon: <FaFileAlt />,
    title: "Balanced Policy Recommendation",
    subtitle: "Stage 06",
    description:
      "The platform combines supporting and opposing viewpoints into balanced policy recommendations.",
    color: "#22C55E",
},
{
    id: 7,
    icon: <FaUniversity />,
    title: "Government Decision Support",
    subtitle: "Stage 07",
    description:
      "Government officials receive clause-wise insights, summaries and recommendations to support informed policy decisions.",
    color: "#2563EB",
},
{
    id: 8,
    icon: <FaGavel />,
    title: "Better Public Policy",
    subtitle: "Outcome",
    description:
      "Data-driven decisions result in fairer, more effective legislation that ultimately benefits citizens.",
    color: "#334155",
},,
];

function Pipeline() {
  return (
    <section className="pipeline">

      <div className="pipeline-heading">

        <h2>How PolicyLens Works</h2>

        <p>
          Transforming citizen participation into structured policy insights
          through a multi-stage machine learning pipeline.
        </p>

      </div>

      <div className="pipeline-container">

        {pipelineSteps.map((step, index) => (

          <div
            key={step.id}
            className={`pipeline-step ${
              index % 2 === 0 ? "left" : "right"
            }`}
          >

            <div
              className="pipeline-circle"
              style={{ background: step.color }}
            >
              {step.icon}
            </div>

            <div className="pipeline-card">

              <span>{step.subtitle}</span>

              <h3>{step.title}</h3>

              <p>{step.description}</p>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}

export default Pipeline;