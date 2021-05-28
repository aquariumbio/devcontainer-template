ARG VARIANT="3.9"
FROM python:${VARIANT}

# create directories within container
# /script is where the package lives
ENV SCRIPT_DIR=/script
WORKDIR ${SCRIPT_DIR}

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp

# copy script into container
COPY ./ .

RUN python3 setup.py develop

# run script by default
ENTRYPOINT ["python3", "/script/template"]
