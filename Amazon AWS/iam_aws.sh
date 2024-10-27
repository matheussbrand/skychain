# Creating a permission policy for API access

aws iam create-policy --policy-name ApiAccessPolicy \
    --policy-document '{
        "Version": "2023-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "execute-api:Invoke",
                "Resource": "arn:aws:execute-api:us-west-2:YOUR_ACCOUNT_ID:YOUR_API_ID/*"
            }
        ]
    }'