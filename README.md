# MovieRecognition
README

Proyecto de Reconocimiento Facial en Películas

Integrantes
- Sharon Tencio Barrantes
- Raschell Jarquín Quesada

Descripción del Proyecto
Este proyecto utiliza tecnologías avanzadas de reconocimiento facial (Roboflow y YOLOv8) para identificar y analizar a cinco actores: Henry Cavill, Will Smith, Jennifer Aniston, Adam Sandler y Angelina Jolie. Además, también detecta la presencia de objetos como pistolas y cuchillos. Con base en la detección de estas personas y objetos, se generan estadísticas sobre su aparición en el video.

Instrucciones de Instalación
Para ejecutar este sistema, es necesario tener instalados los siguientes programas:

1. Visual Studio Code
2. REACT
3. Node.js y npm
4. Python 3.7 o una versión superior

Pasos de Instalación
1. Clonar el repositorio:
   > git clone https://github.com/usuario/proyecto-reconocimiento-facial.git
   > cd proyecto-reconocimiento-facial
   

2. Instalar Visual Studio Code:
   Descargar e instalar Visual Studio Code en: (https://code.visualstudio.com/)

3. Instalar Node.js y npm:
   Descargar e instalar Node.js en: (https://nodejs.org/)

4. Instalar Python:
   Descargar e instalar Python en: (https://www.python.org/)

Guía de uso
El frontend está desarrollado utilizando REACT para proporcionar una interfaz amigable con el usuario. Para la ejecución de este se debe ejecutar los siguientes comandos en la terminal del proyecto:

1. Navegar al directorio del frontend:
   > cd recognition

2. Instalar las dependencias de Node.js:
   > npm install
 

3. Iniciar la aplicación REACT:
   > npm start

Configuración del Backend
El backend utiliza Flask para manejar las solicitudes y ejecutar el modelo de reconocimiento.

1. Navegar al directorio del backend:
   > cd backend


2. Ejecutar el servidor Flask:
   > python main.py

Ejecutar la Aplicación
Una vez que el frontend y el backend están configurados y ejecutándose, abre tu navegador y accede a la siguiente dirección para interactuar con la aplicación:
http://localhost:3000

Nota
El modelo proporcionado está entrenado para detectar a los cinco actores mencionados y dos tipos de objetos (pistolas y cuchillos). Sin embargo, puedes entrenar tu propio modelo utilizando YOLO y reemplazar el modelo existente con el tuyo.
