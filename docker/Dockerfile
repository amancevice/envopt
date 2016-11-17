FROM python:alpine

RUN pip install envopt

ENV ENVOPT_PREFIX=MYSCRIPT_ \
    MYSCRIPT_OPTION_A='I was set in the Dockerfile' \
    MYSCRIPT_OPTION_B='I was also set in the Dockerfile'

COPY myscript.py .

ENTRYPOINT ["python", "myscript.py"]
