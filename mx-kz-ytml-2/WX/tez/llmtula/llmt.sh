#!/usr/bin/bash
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

# Tokei Tooling use - Summay stats of code
tokei1() {
    hea1 "Tokei Use"
    co1="tokei -s Code ../../.."
    echo -e "${GREEN}Command: ${NC}${co1}"
    eval "$co1"
}

# cocomo - Like tokei but brief
cocomo1() {
    hea1 "cocomo Use"
    co1="cocomo ../../.."
    echo -e "${GREEN}Command: ${NC}${co1}"
    eval "$co1"
}

# quagga - Combine files for llms
#
quagga() {
    hea1 "quagga Use"
    co1="quagga ../.. \
    --max-total-size=10485160  \
    --max-part-size=1048576  \
    --output q_out.txt "
    echo -e "${GREEN}Command: ${NC}${co1}"
    eval "$co1"
}

# --- Execution  ---
tokei1
cocomo1
# quagga
