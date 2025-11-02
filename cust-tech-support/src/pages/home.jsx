import React from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";

const HomePage = ()=> {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen w-full flex flex-col justify-center items-center bg-gradient-to-br from-blue-700 via-blue-600 to-blue-800 text-white">
  <h1 className="text-4xl font-extrabold mb-12 tracking-wide drop-shadow-lg">
    Welcome to Nokia Portal
  </h1>

  <div className="flex flex-col gap-8 w-80">
    <Button
      className="text-lg py-6 font-semibold bg-white text-blue-800 hover:bg-blue-100 transition-all duration-200 shadow-lg rounded-xl"
      onClick={() => navigate("/login/customer-tech-support")}
    >
      Nokia Customer Tech Team
    </Button>

    <Button
      className="text-lg py-6 font-semibold bg-blue-600 text-white hover:bg-blue-500 transition-all duration-200 shadow-lg rounded-xl"
      onClick={() => navigate("/login/customer-support")}
    >
      Nokia Customer Support
    </Button>
  </div>

  <footer className="absolute bottom-6 text-sm text-blue-100">
    © {new Date().getFullYear()} Nokia Customer Portal
  </footer>
</div>

  );
}

export default HomePage;
