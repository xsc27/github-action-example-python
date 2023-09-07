ARG PY_VER=3
FROM docker.io/python:${PY_VER}-alpine as build
ARG VERSION=0
COPY ** /opt/src/
RUN set -eux && \
  pip config --global set global.progress_bar off && \
  pip config --global set global.root_user_action ignore && \
  SETUPTOOLS_SCM_PRETEND_VERSION=${VERSION} \
    pip install --compile --target /opt/app --constraint /opt/src/constraints.txt /opt/src

FROM docker.io/python:3.11-alpine
COPY --from=build /opt/app/ /opt/app/
USER guest
ENV PYTHONPATH=/opt/app/
ENTRYPOINT ["/opt/app/bin/httpcat"]

LABEL org.opencontainers.image.authors="hire@carlosmeza.com"
