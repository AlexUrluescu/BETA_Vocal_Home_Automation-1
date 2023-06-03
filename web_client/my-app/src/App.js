
import './App.css';

import { useState, useEffect } from 'react'

function App() {

  const [ data, setData ] = useState([])
  const [ dataTest, setDataTest ] = useState([])

  useEffect(() => {

    const fetchData = async () => {
      const res = await fetch('http://localhost:5000/get_data');
      const data1 = await res.json()

      setData(data1)
      console.log(data1);
    }

    fetchData()
  }, [])

  const handleButton = async () => {
      const res = await fetch('http://localhost:5000/get_data');
      const data2 = await res.json()

      setDataTest(data2)
      console.log(data2);
  }
 
  return (
    <div className="App">
      <h1>Hello</h1>
      <div>
        {data.map((el) => (
          <div key={el.id}>
            <p>{el.temperature}</p>
            <p>{el.humidity}</p>
          </div>
        ))}
      </div>

      <div>
        <button onClick={handleButton}>Incarca</button>
          <div>
            {dataTest.length === 0 ? <h1>Nu avem date</h1> : (
              <div>
                {data.map((el) => (
                  <div key={el.id}>
                    <p>{el.temperature}</p>
                    <p>{el.humidity}</p>
                  </div>
                ))}
              </div>
            )}
          </div>
      </div>
    </div>
  );
}

export default App;
