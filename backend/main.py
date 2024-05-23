from flask import Flask, request, jsonify
import divisor_video
import procesar_video
import analizador_video
import logging
from flask_cors import CORS

#Usamos flask para el backend de la app
app = Flask(__name__)
CORS(app)

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_default_video():
    try:
        #Se va a ir indicando en que parte del proceso se encuentra el video
        logging.info("Dividiendo video predeterminado...")
        divided_videos = divisor_video.split_video('C:\\Users\\Usuario\\Desktop\\MovieRec\\MovieRecognition\\backend\\trailer2.mp4', 4)
        
        logging.info("Procesando videos divididos...")
        results_dict = procesar_video.process_videos_with_threading(divided_videos, 'reporte1')
        
        logging.info("Analizando resultados...")
        analysis_results = analizador_video.plot_class_and_general_stats(results_dict)
        return analysis_results 
    
    except Exception as e:
        logging.error(f"Error en el procesamiento de videos: {e}")
        return {"error": str(e)}


@app.route('/process_videos', methods=['POST'])
def analizador_videos():
    analysis_results = process_default_video()
    return jsonify(analysis_results)

if __name__ == '__main__':
    # Procesar el video predeterminado al iniciar el servidor Flask
    #process_default_video()
    # Iniciar el servidor Flask
    app.run(debug=True)
