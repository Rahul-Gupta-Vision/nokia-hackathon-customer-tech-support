import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import HomePage from "./pages/home"
import LoginPageCustomerTech, {LoginPageCustomerSupport} from "./pages/customer-tech-team-login"
import ChatPage from "./pages/chat"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login/customer-tech-support" element={<LoginPageCustomerTech />} />
        <Route path="/login/customer-support" element={<LoginPageCustomerSupport/>}/>
        <Route path="/chat" element={<ChatPage/>}/>
      </Routes>
    </Router>
  )
}

export default App
