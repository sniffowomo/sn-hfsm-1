#!/usr/bin/bash
# Woman Ass Candy
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

# Vercel Cli Install
ver_cli() {
    hea1 "Install Verpanty"

    CO1="bun add -g vercel"

    ## RUN Above Commands
    echo -e "--- Executing ${CO1} ---"
    eval "$CO1"
    echo -e "${GREEN}***** Raping Completed *****${NC}"
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

    DEPS="rich gradio[mcp] smolagents[toolkit] dotenv"
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

# Initialize new nextjs project
njs1() {
    hea1 "NextJS Install - bunx"
    co1="bunx create-next-app@latest"
    echo -e "--- Executing ${co1} ---"
    eval "$co1"
}

# Execution
ver_cli
# uv_gr
