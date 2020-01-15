FROM grahamdumpleton/mod-wsgi-docker:python-3.5

WORKDIR /app

RUN mod_wsgi-docker-build

COPY requirements.txt /app

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . /app

ENTRYPOINT [ "mod_wsgi-docker-start" ]
