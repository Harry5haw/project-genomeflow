# Start from the official Airflow image
FROM apache/airflow:2.8.1

# Switch to the root user to install things
USER root

# Create a directory for our requirements
RUN mkdir -p /opt/airflow/requirements

# Copy our local requirements.txt file into the container
COPY requirements.txt /opt/airflow/requirements/

# Switch back to the airflow user
USER airflow

# Install the packages from our requirements.txt file
RUN pip install --no-cache-dir -r /opt/airflow/requirements/requirements.txt