# CK Faust distributed project

This project contains a minimal distributed Faust application that runs on Kafka.

## Structure

- `app/` - Faust application package, including producer and worker modules
- `docker-compose.yml` - Kafka, Zookeeper, Faust worker, and producer services
- `requirements.txt` - Python dependencies for Faust
- `.gitignore` - Python and environment ignores

## Run locally with Docker Compose

1. Start Kafka and the Faust worker:

   ```bash
   docker compose up --build
   ```

2. In another terminal, run the producer service to send sample events:

   ```bash
   docker compose run --rm producer
   ```

3. Watch the worker logs for processed event output.

## Files

- `app/__init__.py` - Faust application definition and stream agent
- `app/producer.py` - sample event producer
- `app/worker.py` - Faust worker entrypoint

## Notes

- Ensure Docker and Docker Compose are installed before running the project.
- Use `docker compose down` to stop the services.
