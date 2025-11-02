# Use official NVIDIA PyTorch image with CUDA 12.1 and cuDNN 8
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Prevent Python from buffering stdout/stderr and writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    poppler-utils \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies + Jupyter
RUN pip install --no-cache-dir jupyter jupyterlab && \
    pip install --no-cache-dir -r requirements.txt

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter Notebook by default
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]