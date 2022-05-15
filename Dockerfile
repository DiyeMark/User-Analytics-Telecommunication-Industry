FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requiremts.txt
EXPOSE 8501
COPY ./app /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]