FROM jupyter/pyspark-notebook

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /tmp/