**Deploy S3, CloudFront and ACM via Cloudformation**  
`aws --region us-east-1 cloudformation deploy --template-file cloudformation.yml --stack-name fabiangeiger`

**Empty S3 bucket**
aws s3 rm s3://fabiangeiger --recursive

**Invalidate Cloudfront**
aws cloudfront create-invalidation --distribution-id TOOD --paths "/*"