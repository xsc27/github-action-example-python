FROM docker.io/python:3.11-alpine
COPY **.py /opt/app/
RUN --mount=type=bind,source=.,target=/mnt/src \
  set -eux &&\
  ls -lahR /mnt && \
  pip install --no-cache-dir -r /mnt/src/requirements.txt && \
  pip install --no-cache-dir -r /mnt/src/
USER guest
ENTRYPOINT ["github-action-example-python"]
