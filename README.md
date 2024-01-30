# Pokedex
Pokedex es una aplicación web que te permite consultar información sobre los Pokémon, sus tipos, sus habilidades, sus movimientos, etc. Usa Django como framework web y la PokeAPI como fuente de datos.

## Funcionalidades
- Listar los primeros 50 Pokémon con su id, nombre, tipos, altura y peso.
- Filtrar los Pokémon por diferentes criterios, como peso, tipo o altura.
- Ver los nombres de los Pokémon invertidos.
- Buscar información detallada sobre un Pokémon específico.

## Requisitos
- Python 3.12
- Django 5.0
- Requests 2.26
- Pokebase 1.2
  
Asegúrate de tener Python y pip instalados en tu sistema. Se recomienda el uso de un entorno virtual para aislar las dependencias del proyecto. Además, el proyecto utiliza las bibliotecas especificadas en el archivo requirements.txt.

# Backend
## Pasos para configurar el entorno virtual
### 1: Clonar el Repositorio: 
```bash
git  clone https://github.com/alexa12mora/Pokedex.git
```

Acceder al proyecto : cd pokedex

### 2: Crear y Activar el Entorno Virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
```


### 3: Instalar Dependencias:
```bash
pip install -r requirements.txt
```


## Configuración de la API
### 1: Ejecutar el Servidor de Desarrollo:
```bash
python manage.py runserver
```

La API estará disponible en http://127.0.0.1:8000/


# Frontend
### Backend y frontend se encuentran en la misma carpeta, no se debe ejecutar en Frontend en el entorno virtual de python

## Pasos para configurar y correr el frontend

## Requisitos

Necesitas tener instalado Node.js y npm en tu máquina.

## Instalación

Primero, instala `http-server` globalmente en tu máquina con el siguiente comando:
```bash
npm install --global http-server
```
## Uso
### Para correr el frontend, sigue estos pasos:

Abre tu terminal.
Navega a la carpeta que contiene tu archivo HTML utilizando el comando cd. Por ejemplo, si tu archivo HTML está en una carpeta llamada mi-proyecto en tu Escritorio, el comando sería algo como esto:

```bash
cd Desktop/mi-proyecto
```
### Inicia el servidor HTTP con el siguiente comando:

```bash
http-server -p 5500
```





