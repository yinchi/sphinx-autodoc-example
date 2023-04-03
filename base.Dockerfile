FROM python:3.11-slim

COPY requirements.txt /requirements.txt
COPY scripts /scripts

RUN apt -y update
RUN apt -y install make
RUN pip install --no-cache-dir -r /requirements.txt

# docker compose run --rm bash docs-clean
RUN chmod +x /scripts/docs-build

# docker compose run --rm bash docs-build
RUN chmod +x /scripts/docs-clean

# docker compose run --rm bash docs-serve -d
RUN chmod +x /scripts/docs-serve

ENV PATH="/scripts:${PATH}"

WORKDIR /app/my_package/

CMD ["bash"]
