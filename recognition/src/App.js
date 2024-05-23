import React, { useState } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';
import './App.css';
import lupa from './analisis.png';

function App() {
  const [results, setResults] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleProcessClick = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await axios.post('http://localhost:5000/process_videos', {
        video_path: 'Je.mp4',
        num_parts: 4,
        save_folder: 'your_save_folder_path' // Puedes cambiarlo según la necesidad
      });
      setResults(response.data);
    } catch (error) {
      setError('Error processing videos: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <div className='caja1'>
        <h1>Reconocimiento facial en películas</h1>
        <img src={lupa} alt="Análisis" />
      </div>
      <div className='caja2'>
        <button className='button' onClick={handleProcessClick} disabled={isLoading}>
          {isLoading ? 'Processing...' : 'Process Video'}
        </button>
        {error && <p style={{ color: 'red', marginTop: '20px' }}>{error}</p>}
        {results && (
          <div className='resultados'>
            <h2>Resultados</h2>
            <div className='graficos'>
              <h3>Gráficos</h3>
              <Plot 
                data={JSON.parse(results.counts_plot).data}
                layout={JSON.parse(results.counts_plot).layout}
              />
              <Plot style={{width: '100%'}}
                data={JSON.parse(results.confidences_plot).data}
                layout={JSON.parse(results.confidences_plot).layout}
              />
            </div>
            <div>
              <h3>Estadísticas</h3>
              <ul>
                {results.stats.map((stat, index) => (
                  <li key={index}>
                    {stat.class}: Cantidad - {stat.count}, Confianza Media - {stat.mean_confidence.toFixed(2)}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
