# face-detector-simapp

Application jouet de détection d'éléments (visage, sourire, yeux, etc.) sur une photo.

Le déploiement du streamlit peut être très compliqué en raison du très gand nombre de librairies à installer. Il devient presque obligatoire de créer un docker pour faciliter le déploiement.

## Launch Streamlit Locally

Lancement de l'application streamlit pour test.

```bash
# get into the app folder
cd app/
# launch streamllit
streamlit run app.py
```

## Build the Docker image

On suppose qu'on se trouve toujours dans le répertoir `app/`

```bash
# get into the app folder
cd app/
# Build the image
docker build -t face-detector-simapp:latest .
```

## Launch the container

```bash
# Run a container
docker run -p 8501:8501 face-detector-simapp:latest
```

Pour regarder à l'intérieur du docker si besoin:

```bash
# interacting with the container
docker exec -it <nom du container> bash
```

Avec la modification dans le Dockerfile:

In development, simply run your container with a `PORT` environment variable and a port mapping like this:

docker run -it MY_DOCKER_IMAGE -p HOST_PORT:CONTAINER_PORT -e PORT=CONTAINER_PORT

`docker run -p 8501:8501 app -e PORT=8501`


Voir aussi: [How to Pass Environment Variables to Docker Containers (howtogeek.com)](https://www.howtogeek.com/devops/how-to-pass-environment-variables-to-docker-containers/)

## Déploiemeent Avec Heroku


1. connexion à heroku:

```
heroku login
```

2. connexion à heroku container

heroku container:login

3. Create une application

heroku create face-detector-simapp ou juste heroku create

Avec la deuxième option heroku va donner un nom aléatoire (dans notre cas il s'agit de safe-ravine-76536)

4. Push de Dockerfile à heroku

```
heroku container:push web --app safe-ravine-76536
```

5. Build the container

```
heroku container:release web --app safe-ravine-76536
```


On obtient alors: [app · Streamlit (safe-ravine-76536.herokuapp.com)](https://safe-ravine-76536.herokuapp.com/)



## ressources

1. [A Code Walk Through to Deploying a Container on Heroku Platform (analyticsvidhya.com)](https://www.analyticsvidhya.com/blog/2021/11/a-code-walk-through-to-deploying-a-container-on-heroku-platform/)
2. [Creating a Streamlit web app, building with Docker + GitHub Actions, and hosting on Heroku | Joshua Cook](https://joshuacook.netlify.app/post/streamlit-app-heroku/)
