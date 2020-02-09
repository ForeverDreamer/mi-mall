FROM grahamdumpleton/mod-wsgi-docker:python-3.5

WORKDIR /app

# RUN mod_wsgi-docker-build

# COPY build.sh /app

# RUN ./build.sh

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

ENTRYPOINT [ "mod_wsgi-docker-start" ]
