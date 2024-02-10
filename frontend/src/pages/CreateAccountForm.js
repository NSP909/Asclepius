import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Lock, LockKeyhole, UserRound } from "lucide-react";

const CreateAccountForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPass, setConfirmPass] = useState("");

  const handleCreate = () => {
    // Handle sign-in logic here
  };

  const handleSigninAccount = () => {
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
          <div className="bg-white p-8 rounded-lg shadow-xl w-[50vw] h-[60vh] max-w-[400px] max-h-[650px]">
            <h2 className="text-2xl font-['Nunito Sans'] font-semibold mb-6 text-gray-800">
              Register
            </h2>
            <div className="mb-6">
              {/* <div className="flex justify-around mb-5">
            <button className="mt-2 p-2 bg-blue-500 text-white rounded-2xl px-4 py-2 hover:bg-blue-600 focus:outline-none focus:bg-blue-600 w-[40%] b-cyan-500 font-semibold">
              Doctor
            </button>
            <button className="mt-2 p-2 bg-blue-500 text-white rounded-2xl px-4 py-2 hover:bg-blue-600 focus:outline-none focus:bg-blue-600 w-[40%] b-cyan-500 font-semibold">
              User
            </button>
          </div> */}
              {/* These buttons are to choose between a doctor/user account, get me a better template lol, they look ass*/}
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
            <div className="mb-6">
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
            </div>
            <div className="mb-6">
              <label
                htmlFor="password"
                className="text-gray-600 font-semibold mb-2 text-left flex gap-1"
              >
                <LockKeyhole /> Confirm Password
              </label>
              <input
                type="password"
                id="password"
                name="password"
                className="w-full border-b border-b-gray-400 rounded px-4 py-1 focus:outline-none focus:border-blue-400"
                onChange={onPasswordChange}
              />
            </div>
            <button
              onClick={handleCreate}
              className="mt-6 bg-blue-500 text-white rounded-2xl px-4 py-2 hover:scale-[1.1] focus:outline-none focus:bg-blue-600 w-[80%] bg-gradient-to-r from-cyan-500 via-purple-500 to-pink-500 font-semibold"
            >
              CREATE
            </button>
            <p className="mt-4 text-sm text-gray-600">
              Already have an account?{" "}
              <Link to="/">
                <button onClick={handleSigninAccount} className="text-blue-500">
                  Sign in
                </button>
              </Link>
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default CreateAccountForm;
