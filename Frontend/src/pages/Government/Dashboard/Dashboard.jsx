import Sidebar from "./Sidebar/Sidebar";
import Topbar from "./Topbar/Topbar";

import "./Dashboard.css";

const Dashboard = () => {
    return (
        <div className="dashboard-layout">

            {/* Sidebar */}

            <Sidebar />

            {/* Main Content */}

            <main className="dashboard-main">

                <Topbar />

                {/* Overview Cards */}

                <section className="dashboard-section">

                    <h2>Overview</h2>

                    <div className="card-grid">

                        <div className="dashboard-card">
                            <h3>Total Articles</h3>
                            <p>58</p>
                        </div>

                        <div className="dashboard-card">
                            <h3>Total Paragraphs</h3>
                            <p>1,842</p>
                        </div>

                        <div className="dashboard-card">
                            <h3>Policies</h3>
                            <p>4</p>
                        </div>

                        <div className="dashboard-card">
                            <h3>Clauses</h3>
                            <p>27</p>
                        </div>

                    </div>

                </section>

                {/* Policy & Media */}

                <section className="dashboard-row">

                    <div className="dashboard-panel">

                        <h2>Policy Overview</h2>

                        <ul>

                            <li>CAA - 52 Articles</li>
                            <li>Farm Laws - 18 Articles</li>
                            <li>DPDP - 26 Articles</li>
                            <li>Waqf Bill - 31 Articles</li>

                        </ul>

                    </div>

                    <div className="dashboard-panel">

                        <h2>Media Distribution</h2>

                        <ul>

                            <li>The Wire - 18 Articles</li>
                            <li>OpIndia - 16 Articles</li>
                            <li>General - 24 Articles</li>

                        </ul>

                    </div>

                </section>

                {/* Stance & Clauses */}

                <section className="dashboard-row">

                    <div className="dashboard-panel">

                        <h2>Stance Distribution</h2>

                        <ul>

                            <li>Support - 42%</li>
                            <li>Oppose - 36%</li>
                            <li>Neutral - 22%</li>

                        </ul>

                    </div>

                    <div className="dashboard-panel">

                        <h2>Most Discussed Clauses</h2>

                        <ul>

                            <li>Clause 3 - 624 Mentions</li>
                            <li>Clause 2 - 581 Mentions</li>
                            <li>Clause 5 - 421 Mentions</li>

                        </ul>

                    </div>

                </section>

                {/* Highest Priority */}

                <section className="dashboard-section">

                    <h2>Highest Priority Paragraphs</h2>

                    <table>

                        <thead>

                            <tr>

                                <th>Priority</th>
                                <th>Article</th>
                                <th>Paragraph</th>

                            </tr>

                        </thead>

                        <tbody>

                            <tr>

                                <td>95</td>
                                <td>CAA Protest Analysis</td>
                                <td>Paragraph 7</td>

                            </tr>

                            <tr>

                                <td>93</td>
                                <td>Citizenship Debate</td>
                                <td>Paragraph 2</td>

                            </tr>

                            <tr>

                                <td>91</td>
                                <td>CAA Explained</td>
                                <td>Paragraph 5</td>

                            </tr>

                        </tbody>

                    </table>

                </section>

                {/* Recent Articles */}

                <section className="dashboard-section">

                    <h2>Recent Articles</h2>

                    <table>

                        <thead>

                            <tr>

                                <th>Title</th>
                                <th>Source</th>
                                <th>Policy</th>
                                <th>Date</th>

                            </tr>

                        </thead>

                        <tbody>

                            <tr>

                                <td>CAA Explained</td>
                                <td>The Wire</td>
                                <td>CAA</td>
                                <td>Today</td>

                            </tr>

                            <tr>

                                <td>Citizenship Debate</td>
                                <td>OpIndia</td>
                                <td>CAA</td>
                                <td>Yesterday</td>

                            </tr>

                            <tr>

                                <td>Supreme Court Hearing</td>
                                <td>General</td>
                                <td>CAA</td>
                                <td>Yesterday</td>

                            </tr>

                        </tbody>

                    </table>

                </section>

            </main>

        </div>
    );
};

export default Dashboard;