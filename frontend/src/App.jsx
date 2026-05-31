import { useState } from 'react'

function App() {
  const [ingredientes, setIngredientes] = useState('');
  const [resultado, setResultado] = useState(null);
  const [cargando, setCargando] = useState(false);

  const buscarReceta = async () => {
    setCargando(true);
    try {
      const respuesta = await fetch(`http://127.0.0.1:8000/buscar?ingredientes=${ingredientes}`);
      const datos = await respuesta.json();
      setResultado(datos);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setCargando(false);
    }
  }

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col items-center py-12 px-4">
      <div className="max-w-md w-full bg-white rounded-2xl shadow-xl p-8">
        <h1 className="text-3xl font-bold text-orange-600 text-center mb-2">🍳 Recetario IA</h1>
        <p className="text-gray-500 text-center mb-8">¿Qué tienes en tu refrigerador?</p>
        
        <div className="space-y-4">
          <input 
            type="text" 
            className="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-orange-500 focus:ring-2 focus:ring-orange-200 outline-none transition"
            placeholder="Ej: Huevo, Jamón, Queso..." 
            value={ingredientes}
            onChange={(e) => setIngredientes(e.target.value)}
          />
          <button 
            onClick={buscarReceta}
            className="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 rounded-lg transition transform active:scale-95"
          >
            {cargando ? 'Buscando...' : 'Generar Receta'}
          </button>
        </div>

        {resultado && (
          <div className="mt-8 p-6 bg-orange-100 rounded-xl border border-orange-200 animate-fade-in">
            <h2 className="text-xl font-bold text-orange-800 mb-2">Receta Sugerida:</h2>
            <p className="text-orange-900 leading-relaxed">{resultado.receta}</p>
            <div className="mt-4 flex items-center text-xs text-orange-700 bg-white/50 p-2 rounded">
              <span className="mr-2">ℹ️</span> {resultado.info}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App