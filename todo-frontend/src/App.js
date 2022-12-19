import './App.css';
import Navbar from './components/navbar/Navbar';
import '@fortawesome/fontawesome-svg-core/styles.css'
import { useEffect } from 'react';
import { useState } from 'react';
import Notelist from './components/Notelist/Notelist';
import Registro from './components/registro/Registro';
import Inicio from './components/Inicio/Inicio';
import { Routes, Route } from 'react-router-dom';

function App() {
  let [loading, setLoading] = useState(true)
  let [data, setData] = useState()
  let url = 'https://jsonplaceholder.typicode.com/users'

  async function loadData() {
    const response = await fetch(url)
    const data = await response.json()
    setData(data)
    setLoading(false)
  }

  useEffect(() => {
    setLoading(true)
    loadData()
    console.log(data);
  }, [])

  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/notas" element={<Notelist loading={loading} data={data}/>} />
        <Route path="/registro" element={<Registro />} />
      </Routes>
    </div>
  );
}

export default App;
