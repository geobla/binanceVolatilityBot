# This line specifies the base image, which is Python 3.10.12 in this case.
FROM python:3.10.12

# This sets the working directory inside the container to /code.
WORKDIR /code

# It copies the contents of the ./src directory from your host machine to /code/src in the container.
COPY ./src ./src

# This copies your requirements.txt file to the working directory in the container.
COPY requirements.txt .

#  It installs the Python packages listed in requirements.txt.
RUN pip install -r requirements.txt

# This copies the remaining files from your host machine 
# (including your Python script and other application files) 
# to the working directory in the container.
COPY . .

# It specifies the command to run your Python application when the container starts.
CMD ["python3", "src/VolatilityBot.py"]
