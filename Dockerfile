FROM python:3.13-slim-bookworm AS builder

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    ca-certificates && \
    apt-get clean

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY . .

COPY ./pyproject.toml ./pyproject.toml

RUN uv sync

# -------------------------------------------------------------------------
# ___  ____ ____ ___  _  _ ____ ___ _ ____ _  _    ____ ___ ____ ____ ____ 
# |__] |__/ |  | |  \ |  | |     |  | |  | |\ |    [__   |  |__| | __ |___ 
# |    |  \ |__| |__/ |__| |___  |  | |__| | \|    ___]  |  |  | |__] |___ 
#                                                                          
# -------------------------------------------------------------------------

# Set environment variables
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_USER=${DB_USER}
ENV DB_HOSTNAME=${DB_HOST_NAME}
ENV API_KEY=${API_KEY}

WORKDIR = /app

COPY . . 
COPY --from=builder /app/.venv .venv

ENV PATH="/app/.venv/bin:${PATH}"

EXPOSE $PORT