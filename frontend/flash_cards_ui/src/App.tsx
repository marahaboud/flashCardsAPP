import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  const handleIncrease = () => {
    const newCount = count + 1;
    setCount(newCount);
  };

  return (
    <>
      <h1>Hi Flash Cards App...</h1>
      <p>{count}</p>
      <button onClick={() => handleIncrease()}>Increase</button>
    </>
  );
}

export default App;
