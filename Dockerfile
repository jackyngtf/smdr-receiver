FROM python:3.11-slim

WORKDIR /app

# Copy the server script
COPY server.py .

# Create the data directory
RUN mkdir /data

# Expose the port
EXPOSE 9000

# Set environment variable for port
ENV SMDR_PORT=9000

# Run the server with unbuffered output so logs show up immediately
CMD ["python", "-u", "server.py"]
