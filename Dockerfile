FROM python:3.8

RUN addgroup --gid 2000 appuser && \
    adduser --system --uid 2000 appuser

# set a directory for the app
ARG SRV_DIR=/usr/src/app
WORKDIR $SRV_DIR

EXPOSE 7101

COPY requirements.txt requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy all files to the directory
COPY . .

RUN chown -R appuser:appuser $SRV_DIR

# run fraudhub app.py
CMD ["python", "./app.py"]