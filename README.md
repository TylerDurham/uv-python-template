
# uv-python-template

# Docker

## Build

``` shell
docker build --build-arg API_KEY=myapikey \
    --build-arg DB_USER=mydbuser \
    --build-arg DB_PASSWORD=mydbpassword \
    --build-arg DB_HOSTNAME=mydbname \
     . -t tylerdurham/uv-python-template
```

## Run

``` shell
docker build --secret id=DB_PASSWORD \
             --secret id=DB_USER \
             --secret id=DB_NAME \
             --secret id=DB_HOST \
             --secret id=ACCESS_TOKEN_SECRET_KEY \
             --target=production \
              . -t tylerdurham/uv-python-template
```