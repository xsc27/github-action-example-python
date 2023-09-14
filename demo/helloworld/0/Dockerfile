ARG PY_VER=3
FROM docker.io/python:${PY_VER}-alpine
COPY --chmod=555 *.py /opt/app/
RUN pip install \
  --root-user-action ignore \
  --progress-bar off \
  --no-cache-dir \
  'pydantic-settings~=2.0.3'
ENTRYPOINT ["/opt/app/main.py"]
LABEL org.opencontainers.image.authors="hire@carlosmeza.com"
