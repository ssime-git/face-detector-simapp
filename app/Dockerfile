FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]
# OR cmd to launch app when container is run
#CMD streamlit run app.py