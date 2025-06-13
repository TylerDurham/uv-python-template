
# Build

``` shell
docker build --build-arg API_KEY=myapikey \
    --build-arg DB_USER=mydbuser \
    --build-arg DB_PASSWORD=mydbpassword \
    --build-arg DB_HOSTNAME=mydbname \
     . -t github.com/tylerdurham/uv-python-template
```