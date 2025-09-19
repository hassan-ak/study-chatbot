# Python base (matches your local 3.13)
FROM python:3.13-slim

# System deps (curl for uv installer; add build tools if you need to compile wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install uv (Astral)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Workdir
WORKDIR /app

# Copy files
COPY . .

# Install deps from uv.lock (fast, reproducible)
RUN uv --version && uv sync --frozen

# Spaces serves on port 7860 by convention, but also provides $PORT.
EXPOSE 7860

# Start Chainlit (bind to 0.0.0.0). Use $PORT if provided, else 7860.
CMD ["bash", "-lc", "uv run chainlit run src/study_chatbot/app.py --host 0.0.0.0 --port ${PORT:-7860}"]
