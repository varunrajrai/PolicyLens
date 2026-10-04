import { Routes, Route, Navigate } from "react-router-dom";

import Landing from "../pages/Landing/Landing";
import Login from "../pages/auth/Login/Login";
import Register from "../pages/auth/Register/Register";

/* ===========================
   Layouts
=========================== */

/* ===========================
   Citizen
=========================== */

import CitizenLayout from "../layouts/CitizenLayout/CitizenLayout";
import GovernmentLayout from "../layouts/GovernmentLayout/GovernmentLayout";

import Dashboard from "../pages/Citizen/Dashboard/Dashboard";
import SubmitArticle from "../pages/Citizen/SubmitArticle/SubmitArticle";
import MyArticles from "../pages/Citizen/MyArticles/MyArticles";
import PolicyReview from "../pages/Citizen/PolicyReview/PolicyReview";
import Profile from "../pages/Citizen/Profile/Profile";

/* ===========================
   Government
=========================== */

import GovernmentDashboard from "../pages/Government/Dashboard/Dashboard";

const AppRoutes = () => {
  return (
    <Routes>

      {/* ===========================
          Public Routes
      ============================ */}

      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      {/* ===========================
          Citizen Routes
      ============================ */}

      <Route element={<CitizenLayout />}>

        <Route
          path="/citizen/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/citizen/submit-article"
          element={<SubmitArticle />}
        />

        <Route
          path="/citizen/my-articles"
          element={<MyArticles />}
        />

        <Route
          path="/citizen/policy-review"
          element={<PolicyReview />}
        />

        <Route
          path="/citizen/policy-review/:articleId"
          element={<PolicyReview />}
        />

        <Route
          path="/citizen/profile"
          element={<Profile />}
        />

      </Route>

      {/* ===========================
          Government Routes
      ============================ */}

      <Route element={<GovernmentLayout />}>

        <Route
          path="/government/dashboard"
          element={<GovernmentDashboard />}
        />

        {/*
        <Route
          path="/government/review-queue"
          element={<ReviewQueue />}
        />

        <Route
          path="/government/policy-management"
          element={<PolicyManagement />}
        />

        <Route
          path="/government/clause-insights"
          element={<ClauseInsights />}
        />

        <Route
          path="/government/media-analysis"
          element={<MediaAnalysis />}
        />

        <Route
          path="/government/analytics"
          element={<Analytics />}
        />

        <Route
          path="/government/profile"
          element={<GovernmentProfile />}
        />
        */}

      </Route>

      {/* ===========================
          404
      ============================ */}

      <Route
        path="*"
        element={<Navigate to="/" replace />}
      />

    </Routes>
  );
};

export default AppRoutes;