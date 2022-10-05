# face-detector-simapp

Application de détection d'éléments (visage, sourire, yeux, etc.) sur une photo


## Launch Streamlit Locally


```
cd app/
streamlit run app.py
```

## Build the image


On suppose qu'on se trouve toujours dans le répertoir app/

```
# lauck the image building
docker build -t face-detector-simapp:latest .
```

## Launch the app

```
docker run -p 8501:8501 face-detector-simapp:latest
```


Pour regarder à l'intérieur du docker: docker exec -it quizzical_mcclintock bash
