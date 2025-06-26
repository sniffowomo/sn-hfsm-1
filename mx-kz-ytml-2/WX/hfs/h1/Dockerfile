# 1. Use Rust base image (Rust pre-installed)
FROM rust:1.80

# 2. Install dependencies for curl, and uv
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 3. Install uv using the official script
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# 4. Add uv to PATH
ENV PATH="/root/.local/bin:${PATH}"

# 5. Create working directory
WORKDIR /app

# 6. Copy your Python code
COPY . .

# 8. Default command to run your app
CMD ["uv", "run", "buty.py"]
