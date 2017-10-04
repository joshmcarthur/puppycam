# puppycam
A little thing I made to check up on foster dogs when I'm not at home

### Components

1. `save_snapshot.py`: A lambda function that runs in reaction to a Cloudwatch Event (a scheduled event invoked once per minute)
2. `index.html`: A page that auto-refreshes with a meta tag to load the latest snapshot fetched by the Lambda function.

### Setup

I'd love to have a script to set up the AWS environment. It's totally possible, but I happened to set this up in the web console,
so I'm not going to go back and figure out the steps. Loosely, you need an S3 bucket to dump the snapshot into (policy provided), and
a Lambda task set up with environment variables saying where to get the image, and what bucket & key to use.
