
# uv-python-template

# Docker

## Build

### Easier

``` shell
docker build --build-arg API_KEY=myapikey \
    --build-arg DB_USERID=mydbuser \
    --build-arg DB_PASSWORD=mydbpassword \
    --build-arg DB_HOSTNAME=mydbname \
     . -t tylerdurham/uv-python-template
```

### Better

Set secrets in ENV:

``` shell
export DB_PASSWORD="mydbpassword" \
export DB_USERID="mydbuser" \
export DB_NAME="mydbname" \
export DB_HOST="mydbhost" \
export ACCESS_TOKEN_SECRET_KEY="mysecretkey"
```

Build the image:

``` shell
docker build --secret id=DB_PASSWORD \
             --secret id=DB_USERID \
             --secret id=DB_NAME \
             --secret id=DB_HOST \
             --secret id=ACCESS_TOKEN_SECRET_KEY \
             --target=production \
              . -t tylerdurham/uv-python-template
```

## Run

``` shell
docker run -v "$(pwd)/logs:/app/logs" -p 8080:8080 tylerdurham/uv-python-template
```

or

``` shell
docker compose up -d
```
