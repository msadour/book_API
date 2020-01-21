FROM django

ADD . .

WORKDIR .

RUN apt-get update && apt-get install -y build-essential pkg-config

RUN python -m pip install -U Django

RUN pip install -r requirements.txt

# RUN createdb library