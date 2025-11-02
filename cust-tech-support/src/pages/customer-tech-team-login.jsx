import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldSet,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

var assistant = "";
const LoginPageCustomerTech = () => {
  const navigate = useNavigate()
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")

  const handleLogin = () => {
    if (username === "admin@nokia.com" && password === "password") {
      assistant = "LoginPageCustomerTech"
      navigate("/chat")
    } else {
      setError("Invalid credentials. Try again.")
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-900 via-blue-700 to-blue-500">
      <div className="w-full max-w-md bg-white/10 backdrop-blur-md p-8 rounded-xl shadow-2xl text-white">
        <h1 className="text-3xl font-bold text-center mb-6">
          Nokia Customer Tech Support Login
        </h1>
        <FieldSet>
          <FieldGroup>
            <Field>
              <FieldLabel htmlFor="username">Username</FieldLabel>
              <Input
                id="username"
                type="text"
                placeholder="admin@nokia.com"
                className="bg-white/20 border-none text-white"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <FieldDescription>Enter your Nokia ID</FieldDescription>
            </Field>
            <Field>
              <FieldLabel htmlFor="password">Password</FieldLabel>
              <Input
                id="password"
                type="password"
                placeholder="password"
                className="bg-white/20 border-none text-white"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <FieldDescription>Use your secure password</FieldDescription>
            </Field>
          </FieldGroup>
        </FieldSet>

        <Button
          className="mt-6 w-full py-4 bg-blue-500 hover:bg-blue-600 text-lg font-semibold rounded-xl"
          onClick={handleLogin}
        >
          Login
        </Button>

        {error && <p className="text-red-400 text-center mt-4">{error}</p>}
      </div>
    </div>
  )
}

export const LoginPageCustomerSupport = () => {
  const navigate = useNavigate()
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")

  const handleLogin = () => {
    if (username === "admin@nokia.com" && password === "password") {
      assistant = "LoginPageCustomerSupport"
      navigate("/chat")
    } else {
      setError("Invalid credentials. Try again.")
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-900 via-blue-700 to-blue-500">
      <div className="w-full max-w-md bg-white/10 backdrop-blur-md p-8 rounded-xl shadow-2xl text-white">
        <h1 className="text-3xl font-bold text-center mb-6">
          Nokia Customer Support Login
        </h1>
        <FieldSet>
          <FieldGroup>
            <Field>
              <FieldLabel htmlFor="username">Username</FieldLabel>
              <Input
                id="username"
                type="text"
                placeholder="admin@nokia.com"
                className="bg-white/20 border-none text-white"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <FieldDescription>Enter your Nokia ID</FieldDescription>
            </Field>
            <Field>
              <FieldLabel htmlFor="password">Password</FieldLabel>
              <Input
                id="password"
                type="password"
                placeholder="password"
                className="bg-white/20 border-none text-white"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <FieldDescription>Use your secure password</FieldDescription>
            </Field>
          </FieldGroup>
        </FieldSet>

        <Button
          className="mt-6 w-full py-4 bg-blue-500 hover:bg-blue-600 text-lg font-semibold rounded-xl"
          onClick={handleLogin}
        >
          Login
        </Button>

        {error && <p className="text-red-400 text-center mt-4">{error}</p>}
      </div>
    </div>
  )
}

export function data(){
  return assistant;
}
export default LoginPageCustomerTech
