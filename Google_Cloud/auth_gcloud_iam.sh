# Command to configure access permissions on Google Cloud using gcloud

gcloud projects add-iam-policy-binding YOU_PROJECT_ID \
    --member='serviceAccount:YOUR_SERVICE_ACCOUNT_EMAIL' \
    --role='roles/owner' \
    --condition=None    
    