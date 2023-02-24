# Creacion de api con fastApi en python conectado a una base de datos MongoDB Atlas


## Requisitos


### Base de datos Mongo Atlas

- Creación de base de datos

  ![creacion de bd en mongo](/img/crearDbMongoAtlas.png)

  ![creacion de db en mongo2](/img/crearDbMongoAtlas2.png)

  ![creacion de dn en mongo3](/img/crearDbMongoAtlas3.png)

- Configuracion para conectarse a DB

  ![configuracion para conectarse a mongo](/img/configConectMongoDbAtlas.png)

  ![configuracion para conectarse a mongo2](/img/configConectMongoDbAtlas2.png)

  ![configuracion para conectarse a mongo3](/img/configConectMongoDbAtlas3.png)

  Esta es la url de conexión que luego vamos a usar desde nuestra app.


### Creacion de ambiente python venv


#### Creacion de ambiente

- Ejecutar:

      python3 -m venv venv
  
  Se necesita tener instalado
  
      sudo apt install python3.10-venv

- Resultado:

    ![creacion de repo venv](/img/creacionAmbientePython.png)


#### Pararse en el ambiente

- Ejecutar : 

      source venv/bin/activate

- Resultado: 
    
    (venv) salo@salo-UX32VD:~/fastApiMongodb$


### Instalacion de dependencias

#### Redes Transformers

- Ejecutar :

      pip install transformers transformers[tf-cpu] transformers[torch]

  Comprobar si esta funcionando correctamente ejecutando

      python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"
  
  Resutado

      [{'label': 'POSITIVE', 'score': 0.9998704195022583}]


#### FastApi y pymongo

Instalamos las dependencias necesarias: fastapi, uvicorn, pymongo.

- Ejecutar :

      pip install fastapi uvicorn pymongo pymongo[srv]

- Resultado :

    ![instalando dependencias](/img/instalandoDependencias.png)


#### Otras dependencias

- Para las variables de entorno

      pip install python-dotenv
    
- Instalar si lo pide (no recuerdo exactamente que hace)

      pip install sentencepiece

## Proyecto

### Configurar variables de entorno

- Crear archivo .env

      URL_MONGO="mongodb+srv://salomongo:<password>@cluster0.0fw9ft9.mongodb.net/chatBoot"

  Donde dice "password" setear el valor configurado en la seguridad de acceso de mongo atlas.

  ![configuracion para conectarse a mongo4](/img/configConectDbMongoAtlas4.png)

### Levantar proyecto

- Ejecutar:

      uvicorn main:app

- Swagger:

  ![swagger api](/img/swaggerApi.png)

- Caso de prueba:

  ![caso de prueba](/img/casoDePrueba.png)
  

## Referencias y documentacion consultada

- Transformers:

  https://huggingface.co/docs/transformers/installation


- FastApi y mongoAtlas:

  https://www.youtube.com/watch?v=MXwcUrI-iss

  https://www.youtube.com/watch?v=4e2VW3Nu-64
