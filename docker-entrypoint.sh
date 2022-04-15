#!/usr/bin/env sh

if [ "$SERVER_DEPLOYMENT_TYPE" = "deployment" ]; then
  uvicorn scrapper:app \
    --host 0.0.0.0 \
    --port 80 \
    --ssl-certfile /certs/server.cert \
    --ssl-keyfile /certs/server.key \
    --no-proxy-headers \
    --no-server-header \
    --no-date-header
elif [ "$SERVER_DEPLOYMENT_TYPE" = "test" ]; then
  uvicorn scrapper:app \
    --host 0.0.0.0 \
    --port 80 \
    --ssl-certfile /certs/server.cert \
    --ssl-keyfile /certs/server.key \
    --no-proxy-headers \
    --no-server-header \
    --no-date-header
fi
