FROM python:alpine

RUN pip install envopt

ENV MYSCRIPT_OPTION_A='I was set in the Dockerfile' \
    MYSCRIPT_OPTION_B='I was also set in the Dockerfile'

COPY myscript.py .

ENTRYPOINT ["python", "myscript.py"]
