## ------------------------------- Builder Stage ------------------------------ ## 
FROM python:3.13-bookworm AS builder

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get install curl -y

# Download the latest installer, install it and then remove it
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

# Set up the UV environment path correctly
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY ./pyproject.toml .

RUN uv sync

## ------------------------------- Production Stage ------------------------------ ##
FROM python:3.13-slim-bookworm AS production

# The following secrets are available during build time
RUN --mount=type=secret,id=DB_PASSWORD \
    --mount=type=secret,id=DB_USERID \
    --mount=type=secret,id=DB_NAME \
    --mount=type=secret,id=DB_HOST \
    --mount=type=secret,id=ACCESS_TOKEN_SECRET_KEY \
    DB_PASSWORD=$(/run/secrets/DB_PASSWORD) \
    DB_USERID=$(cat /run/secrets/DB_USERID) \
    DB_NAME=$(cat /run/secrets/DB_NAME) \
    DB_HOST=$(cat /run/secrets/DB_HOST) \
    ACCESS_TOKEN_SECRET_KEY=$(cat /run/secrets/ACCESS_TOKEN_SECRET_KEY)

RUN --mount=type=secret,id=secret-key,target=secrets.json

RUN useradd --create-home appuser
USER appuser

WORKDIR /app

COPY /src .
COPY --from=builder /app/.venv .venv

# Set up environment variables for production
ENV PATH="/app/.venv/bin:$PATH"

# Expose the specified port for FastAPI
EXPOSE $PORT

# Start the application with Uvicorn in production mode, using environment variable references
CMD ["uvicorn", "my_svc.main:app", "--host", "0.0.0.0", "--log-level", "info", "--port", "8080"]




