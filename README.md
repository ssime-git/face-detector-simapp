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

``` bash
# get into the app folder
cd app/
# Build the image
docker build -t face-detector-simapp:latest .
```

## Launch the container

``` bash
# Run a container
docker run -p 8501:8501 face-detector-simapp:latest
```

Pour regarder à l'intérieur du docker si besoin: 

``` bash
# interacting with the container
docker exec -it <nom du container> bash
```