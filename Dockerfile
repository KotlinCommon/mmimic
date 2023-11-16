FROM python:3.10.12

WORKDIR /app
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt


# Install any additional packages
#RUN /app/venv/bin/python setup.py install

# Specify the command to run your application
CMD ["python", "/app/src/python/application/Application.py"]
