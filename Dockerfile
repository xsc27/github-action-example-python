FROM python:3-alpine
ENV PIP_ROOT_USER_ACTION=ignore \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=/opt/app
COPY requirements.txt $PYTHONPATH/
RUN pip3 --no-cache-dir install \
  -r "$PYTHONPATH/requirements.txt" \
  --target "$PYTHONPATH"
COPY action.py main.py $PYTHONPATH/
CMD $PYTHONPATH/action.py
