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
# UV Setup

uv_gr() {
    hea1 "UV Installation with gradio"

    # Get Name of project
    echo -e "Enter the name of the project: "
    read name_of_project
    if [ -z "$name_of_project" ]; then
        echo -e "${RED}BASTARD ! Project name cannot be empty${NC}"
        exit 1
    fi

    # UC Commands
    CO1="uv init $name_of_project"
    CO2="cd $name_of_project"

    DEPS="rich gradio[mcp] smolagents[toolkit] dotenv groq"
    CO3="uv add  $DEPS"
    CO4="uv tree"

    ## RUN Above Commands
    echo -e "--- Executing ${CO1} ---"
    eval "$CO1"
    echo -e "--- Executing ${CO2} ---"
    eval "$CO2"
    echo -e "--- Executing ${CO3} ---"
    eval "$CO3"
    echo -e "--- Executing ${CO4} ---"
    eval "$CO4"
    echo -e "${GREEN}***** Installation Completed *****${NC}"
}

# Function remove all directories with .vent
rm_venv_find() {
    hea1 "Removing all directories with .venv"
    co1="find . -type d -name '.venv' -exec rm -rf {} +"
    echo -e "--- Executing ${co1} ---"
    eval "${co1}"
}

# Brwoser Use Install Info
brw_in() {
    hea1 "Browser Use Install"

    DEPS="rich dotenv browser-use"

    # Get Name of project
    echo -e "Enter the name of the project: "
    read name_of_project
    if [ -z "$name_of_project" ]; then
        echo -e "${RED}BASTARD ! Project name cannot be empty${NC}"
        exit 1
    fi

    co1="uv init $name_of_project"
    co2="cd $name_of_project"
    co3="uv add $DEPS"
    co4="source .venv/bin/activate.fish"
    co5="playwright install chromium --with-deps --no-shell"
    co6="uv tree"

    ## RUN Above Commands
    echo -e "--- Executing ${co1} ---"
    eval "$co1"
    echo -e "--- Executing ${co2} ---"
    eval "$co2"
    echo -e "--- Executing ${co3} ---"
    eval "$co3"
    echo -e "--- Executing ${co4} ---"
    eval "$co4"
    echo -e "--- Executing ${co5} ---"
    eval "$co5"
    echo -e "--- Executing ${co6} ---"
    eval "$co6"
    echo -e "${GREEN}***** Installation Completed *****${NC}"
}

# Execution
# uv_gr
# rm_venv_find
brw_in
