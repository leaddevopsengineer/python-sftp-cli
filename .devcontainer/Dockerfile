# Use the official Ubuntu 20.04 image as the base image
FROM ubuntu:20.04

# Update and install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    nano \
    python3 \
    python3-pip \
    python3-venv

# Install the AWS CLI
RUN pip3 install awscli --upgrade --user

# Install the Code Server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Copy the devcontainer.json file
COPY devcontainer.json /root/.local/share/code-server/

# Create a new user and set the working directory
RUN useradd -m codespaces
USER codespaces
WORKDIR /home/codespaces

# Expose the default Code Server port
EXPOSE 8443

# Start the Code Server
CMD ["code-server", "--bind-addr", "0.0.0.0:8443", "--user-data-dir", "/root/.local/share/code-server"]
