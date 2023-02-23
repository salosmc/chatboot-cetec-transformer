### Fuente
https://www.youtube.com/watch?v=MXwcUrI-iss

# Creacion de api con fastApi en python conectado a una base de datos MongoDB Atlas

## Requisitos

### Creación de base de datos

- ![creacion de bd en mongo](/img/crearDbMongoAtlas.png)

- ![creacion de db en mongo2](/img/crearDbMongoAtlas2.png)

- ![creacion de dn en mongo3](/img/crearDbMongoAtlas3.png)

### Configuracion para conectarse a DB

- ![configuracion para conectarse a mongo](/img/configConectMongoDbAtlas.png)

- ![configuracion para conectarse a mongo2](/img/configConectMongoDbAtlas2.png)

- ![configuracion para conectarse a mongo3](/img/configConectMongoDbAtlas3.png)

- ![configuracion para conectarse a mongo4](/img/configConectDbMongoAtlas4.png)

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
