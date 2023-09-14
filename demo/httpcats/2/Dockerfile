ARG PY_VER=3
FROM docker.io/python:${PY_VER}-alpine
COPY main.py README.md pyproject.toml /opt/src/
RUN pip install \
  --root-user-action ignore \
  --progress-bar off \
  --no-cache-dir \
  --target /opt/app /opt/src
copy action.py /opt/app/
ENV PYTHONPATH=/opt/app/
ENTRYPOINT ["/opt/app/bin/httpcats"]

LABEL org.opencontainers.image.authors="hire@carlosmeza.com"
