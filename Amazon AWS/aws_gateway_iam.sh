# Command to configure HTTPS for API in AWS API Gateway

aws apigateway create-domain-name \
    --domain-name 'example.com' \
    --certificate-arn arn:aws:acm:us-west-2:YOUR_ACCOUNT_ID:certificate/YOU_CERTIFICATE_ID'