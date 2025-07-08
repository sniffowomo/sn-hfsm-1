#!/usr/bin/bash
# This bash srcript is for installing the KL docker image here
clear

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[0;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[0;37m'
export NC='\033[0m' # No Color

# Commands

hea1() {
  echo -e "${CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${NC}"
  echo -e "${PURPLE}$1${NC}"
  echo -e "${CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~${NC}"
}

# Execution Zone
ru1() {
  hea1 "Execute UV "
  co1="uv run buty.py"
  echo -e "${GREEN} Executing... "
  echo -e " ${co1} ${NC}"
  eval "${co1}"
}

# DockerRun
dockrun_once() {
  IMAGE_NAME="my-app"

  echo "🛠  Building image..."
  docker build -t "$IMAGE_NAME" . || return 1

  echo "🚀 Running container..."
  docker run --rm "$IMAGE_NAME"

  echo "🧹 Removing image..."
  docker rmi "$IMAGE_NAME" >/dev/null || echo "⚠️ Failed to remove image"
}

# Exection
ru1
# dockrun_once
