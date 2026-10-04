import Navbar from "../../components/Common/Navbar/Navbar";
import Hero from "../../components/landing/Hero/Hero";
import Pipeline from "../../components/landing/Pipeline/Pipeline";
import Features from "../../components/landing/Features/Features";
import RoleSelection from "../../components/landing/RoleSelection/RoleSelection";
import Footer from "../../components/Common/Footer/Footer";

function Landing() {
  return (
    <>
      <Navbar />
      <Hero />
      <Pipeline />
      <Features />
      <RoleSelection />
      <Footer />
    </>
  );
}

export default Landing;
