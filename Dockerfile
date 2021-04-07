# Base image
FROM python:3.9.4-slim-buster

# Install dependencies
COPY 'requirements.txt' '/tcpclient/requirements.txt'
WORKDIR /tcpclient
RUN pip install --no-cache-dir -r requirements.txt

# Copy necesary files to the container
COPY 'tcpclient.py' '/tcpclient/tcpclient.py'

# Start python script with unbuffered output option
CMD [ "python", "-u", "/tcpclient/tcpclient.py" ]
