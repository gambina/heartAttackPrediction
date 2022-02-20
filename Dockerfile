FROM python:3.9-buster
# Install the ODBC drivers
RUN apt-get update
RUN apt-get install -y gcc unixodbc-dev nano
# Set the working directory
WORKDIR /app

# Add requirements and install
RUN apt-get update -y

COPY . . 

RUN pip install -r /app/requirements.txt

CMD [ "python3", "-u", "orchestrator.py" ]