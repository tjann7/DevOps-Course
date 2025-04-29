FROM python:3.13.1-alpine3.21

# Environment variables
ENV ADMIN_USER="admin" \
    APP_HOME="/app"

# Create admin user and directories
RUN adduser -D $ADMIN_USER && \
    mkdir -p $APP_HOME /data && \
    chown -R $ADMIN_USER $APP_HOME /data

WORKDIR $APP_HOME

# Install dependencies
COPY --chown=$ADMIN_USER requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY --chown=$ADMIN_USER templates ./templates
COPY --chown=$ADMIN_USER moscow_app.py .

# Final setup
USER $ADMIN_USER
EXPOSE 5000 5005

# Explicit absolute path to Python executable
CMD ["/usr/local/bin/python", "moscow_app.py"]