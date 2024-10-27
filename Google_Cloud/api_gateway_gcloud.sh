# Command to configure HTTPS on Google Cloud
gcloud api-gateway gateways create my-gateway \
    --api=my-api --api-config=my-api-config \
    --location=us-central1 --project=YOUR_PROJECT_ID