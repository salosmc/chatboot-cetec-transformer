### Fuente
https://www.youtube.com/watch?v=MXwcUrI-iss

# Creacion de api con fastApi en python conectado a una base de datos MongoDB Atlas

## Requisitos

### Creación de base de datos

### Configuracion para conectarse a DB

### Creacion de ambiente python venv

#### Creacion de ambiente

- Ejecutar:

      $ python3 -m venv venv

- Resultado:

    ![creacion de repo venv](/img/creacionAmbientePython.png)

#### Pararse en ambiente

- Ejecutar : 

      $ source venv/bin/activate

- Resultado: 
    
    (venv) salo@salo-UX32VD:~/fastApiMongodb$ 

### Instalacion de dependencias

Faltan :

- https://huggingface.co/docs/transformers/installation
- pip install sentencepiece

Instalamos las dependencias necesarias: fastapi, uvicorn, pymongo.

- Ejecutar :

      pip install fastapi uvicorn pymongo pymongo[srv]

- Resultado :

    ![instalando dependencias](/img/instalandoDependencias.png)

## Proyecto 

### Levantar proyecto

- Ejecutar:

      uvicorn main:app

### Esquema de repositorios
