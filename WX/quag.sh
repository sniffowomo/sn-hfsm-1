#!/usr/bin/bash
#  Using quagga for compressing many files into one
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

qua_install() {
    hea1 "Quagga Install"
    co1="cargo install quagga"
    echo -e "--- Executing ${co1} ---"
    eval "${co1}"
}

# Compresses all files int one text file
qua_compress1() {
    hea1 "Quagga Compress"
    # Get name of the file
    echo -e "${PURPLE}Enter name of Output Text file - dir/file_name"
    read file_name
    if [ -z "$file_name" ]; then
        echo -e "${RED}BASTARD ! File name cannot be empty${NC}"
        exit 1
    fi

    co1="quagga \
    --max-part-size=10000000000 \
    --output ${file_name}.txt"
    echo -e "--- Executing ${co1} ---"
    eval "${co1}"
}

# Execute
qua_install
qua_compress1
