# SMDR Receiver (Dockerized)

A lightweight Dockerized Python service to receive Avaya IP Office SMDR records and save them to CSV files. This replaces the legacy Windows Service found [here](https://davehope.co.uk/projects/smdr-receiver/).

## Features
- Listens on TCP Port 9000 (configurable).
- Captures raw SMDR data stream.
- Rotates log files daily (e.g., `smdr_2025-01-12.csv`).
- Runs as a Docker container (compatible with Synology NAS/x86).

## Prerequisites
- Docker Engine
- Docker Compose

## Quick Start
1.  Clone this repository to your NAS (e.g., into `docker/smdr-receiver`).
2.  Run the container:
    ```bash
    docker-compose up -d --build
    ```
3.  The service will start listening on port **9000**.

## Configuration
### Docker Volume
By default, the `docker-compose.yml` maps a local `./data` folder to `/data` inside the container.
On your NAS setup, ensure the volume is mapped correctly so you can access the logs.
- **NAS Path**: `docker/smdr-receiver` (or your preferred location)
- **Container Path**: `/data`

### Avaya IP Office Setup
Configure your Avaya IP Office SMDR settings to point to your NAS IP address.
- **IP Address**: `10.10.206.7` (Your NAS IP)
- **TCP Port**: `9000`
- **Record Output**: `SMDR`

## Files
- `server.py`: The main Python script.
- `data/`: Directory where CSV logs are stored (mapped volume).
