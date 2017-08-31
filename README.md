# Shorten My Link
Shorten My Link is an API to shortern URLs.

## Example usage
Make a `POST` request to `https://shorten-my-link.herokuapp.com/shorten_url` with the request body:
```
{
  "url": "https://really-really-really-long-unwieldy-url.com"
}
```

The response will be:
```
{
  "shortened_url": "https://shorten-my-link.herokuapp.com/<short_id>"
}
```
where `<short_id>` is a random alphanumeric string. Navigate to `https://shorten-my-link.herokuapp.com/<short_id>` in your browser and you will be re-directed to `https://really-really-really-long-unwieldy-url.com`.

## Scalability
This API is currently written as a Python [Django](https://www.djangoproject.com/) application, hosted on [Heroku](https://heroku.com)'s free plan. Data is stored in [PostgreSQL](https://www.postgresql.org/) running on a separate server (also hosted on Heroku). There are multiple ways of scaling the API to production scale. These are, in increasing levels of scalability:

1. Increase the server size and utilise ulti-threading.
2. Deploy the application to multiple servers behind a load balancer (e.g. [Amazon EC2](https://aws.amazon.com/ec2/) + [Elastic Load Balancer](https://aws.amazon.com/elasticloadbalancing/)).
3. Elastically scale the number of servers to meet increasing demand.
4. Add additional database replications on additional servers and balance load between them. For PostgreSQL, [Slony](http://slony.info/) and [pgpool](http://www.pgpool.net/mediawiki/index.php/Main_Page) are useful tools for replication and connection pooling, respectively.
5. Deploy multiple servers behind multiple load balancers.

An entirely different approach to scaling is to write the API as a set of functions to run as part of a serverless architecture, for example using [AWS Lambda](https://aws.amazon.com/lambda/).
