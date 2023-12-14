# Use an official Python runtime as a parent image
FROM python:3.8.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install build dependencies for TA-Lib
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        wget \
        && \
    rm -rf /var/lib/apt/lists/*

# Download and install TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib-0.4.0-src*

# Set the environment variable for TA-Lib
ENV LD_LIBRARY_PATH /usr/local/lib

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
#EXPOSE 5000



# Run app.py when the container launches
CMD ["python3", "app.py"]

