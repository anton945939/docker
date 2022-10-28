# Export variables

export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_REGION="eu-west-3"

# Log ecr

`aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 293038174526.dkr.ecr.eu-west-3.amazonaws.com`

# Docker build

`docker build . -t 293038174526.dkr.ecr.eu-west-3.amazonaws.com/daniel-dev:2`

# Docker push

`docker push 293038174526.dkr.ecr.eu-west-3.amazonaws.com/daniel-dev:2`