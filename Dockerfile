# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

# Environment variables
ENV BOT_NAME="SimpleBot"
ENV PORT=5000

# Expose Flask port
EXPOSE 5000

# Run bot
CMD ["python", "bot.py"]
