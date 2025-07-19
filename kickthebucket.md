Given s3_presigned_url.txt and s3_resource_policy.txt

One gives the url, the other the resource policy, which requires the HTTP request to have `User-Agent: aws-sdk-go....`

Use Burpsuite and change the user agent as follows and solved.