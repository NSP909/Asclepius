import React, { useState } from 'react';
import { UserRound } from "lucide-react";
import { Lock } from "lucide-react";
import {Link} from "react-router-dom";


const AuthenticationForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const handleSignIn = () => {
    // Handle sign-in logic here
  };

  const handleCreateAccount = () => {
    // Handle navigation to create account page
  };

  const onUserNameChange = (e) => {
    setUsername(e.target.value);
    console.log(username);
  };

  const onPasswordChange = (e) => {
    setPassword(e.target.value);
    console.log(password);
  };

  return (
    <>
    <div className="w-full h-screen bg-gradient-to-br from-cyan-500 via-purple-500 to-pink-500">
    <div className="flex flex-col items-center justify-center h-[80vh]">
      <div className="bg-white p-8 rounded-lg shadow-xl w-[50vw] h-[60vh] max-w-[400px] max-h-[500px]">
        <h2 className="text-2xl font-['Nunito Sans'] font-semibold mb-7 text-gray-800">
          Login
        </h2>
        <div className="mb-10">
          <label
            htmlFor="username"
            className="text-gray-600 font-semibold mb-2 text-left flex gap-1"
          >
            {" "}
            <UserRound /> Username
          </label>
          <input
            type="text"
            id="username"
            name="username"
            className="w-full border-b border-b-gray-400 px-4 py-1 focus:outline-none focus:border-blue-400"
            onChange={onUserNameChange}
          />
        </div>
        <div className="mb-5">
          <label
            htmlFor="password"
            className="text-gray-600 font-semibold mb-2 text-left flex gap-1"
            
          >
            <Lock /> Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            className="w-full border-b border-b-gray-400 rounded px-4 py-1 focus:outline-none focus:border-blue-400"
            onChange={onPasswordChange}
          />
          <p className="mt-1 text-sm text-right">
            {" "}
            <button className="text-gray-600">
              Forgot Password?
            </button>
          </p>
        </div>
        <button
          onClick={handleSignIn}
          className="mt-6 bg-blue-500 text-white rounded-2xl px-4 py-2 hover:scale-[1.1] focus:outline-none focus:bg-blue-600 w-[80%] bg-gradient-to-r from-cyan-500 via-purple-500 to-pink-500 font-semibold"
        >
          LOGIN
        </button>
        <p className="mt-4 text-sm text-gray-600">
          Don't have an account?{" "}
          <Link to="/create">
            <button className="text-blue-500">
              Create one
            </button>
          </Link>
        </p>
      </div>
    </div>
    </div>
    </>
  );
};

export default AuthenticationForm;
