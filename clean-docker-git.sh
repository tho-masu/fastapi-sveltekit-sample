#!/bin/bash

docker compose down
docker system prune -af
git clean -xdf
