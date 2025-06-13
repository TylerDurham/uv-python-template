
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


``` shell
docker build --secret id=DB_PASSWORD \
             --secret id=DB_USER \
             --secret id=DB_NAME \
             --secret id=DB_HOST \
             --secret id=ACCESS_TOKEN_SECRET_KEY \
             --target=production \
              . -t tylerdurham/uv-python-template
```

## Run

``` shell
export DB_PASSWORD="mydbpassword"
export DB_USER="mydbuser"
export DB_NAME="mydbname"
export DB_HOST="mydbhost"
export ACCESS_TOKEN_SECRET_KEY="mysecretkey"
```

``` shell
docker run -p 8080:8080 tylerdurham/uv-python-template
```