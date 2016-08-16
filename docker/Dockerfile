FROM python:alpine

RUN pip install envopt

ENV MYSCRIPT_OPTION_A='I started life in the Dockerfile' \
    MYSCRIPT_OPTION_B='I also started life in the Dockerfile'

COPY myscript.py .

ENTRYPOINT ["python", "myscript.py"]
