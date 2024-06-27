# Fastly CDN and WAF Test Server

This project provides a multipurpose webserver deployed on Google Cloud Run for testing Fastly CDN and WAF features. It's designed to remain within the Google Cloud free tier for low-traffic testing scenarios.

## Project Overview

This containerized application includes:

- A static file server (Nginx)
- A dynamic content generator (Flask)
- An API endpoint (Flask)
- Various URL paths to test different Fastly features

## Prerequisites

- Google Cloud Platform account
- gcloud CLI installed and configured
- Docker installed locally (optional, for local testing)

## File Structure

- `Dockerfile`: Defines the container image
- `nginx.conf`: Nginx configuration file
- `app.py`: Flask application for dynamic content and API
- `static/`: Directory containing static files
- `README.md`: This file

## Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/fastly-test-server.git
   cd fastly-test-server
   ```

2. Enable required Google Cloud APIs:
   ```
   gcloud services enable cloudbuild.googleapis.com run.googleapis.com
   ```

3. Build and deploy the container:
   ```
   gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/fastly-test-server
   gcloud run deploy fastly-test-server --image gcr.io/$(gcloud config get-value project)/fastly-test-server --platform managed --allow-unauthenticated --port=8080
   ```

4. Note the URL provided in the output. This is your origin server URL.

## Usage

The server provides several endpoints for testing different scenarios:

- `/`: Serves static HTML content
- `/static/`: Serves static assets with caching headers
- `/dynamic/`: Generates dynamic content
- `/api/`: Provides JSON responses
- `/large-file`: Serves a large file (100MB) to test large file handling
- `/compressed`: Serves pre-compressed content
- `/video`: Serves video content
- `/error/404`: Simulates a 404 error
- `/error/500`: Simulates a 500 error
- `/slow`: Simulates a slow response (5-second delay)
- `/custom-headers`: Returns custom headers
- `/vary-test`: Demonstrates content varying based on request headers
- `/auth`: Basic auth-protected endpoint
- `/cors`: Endpoint with CORS headers
- `/websocket`: WebSocket endpoint

## Fastly Integration

To test with Fastly CDN and WAF:

1. Create a new Fastly service
2. Set the origin to your Cloud Run service URL
3. Configure Fastly's caching rules:
   - Aggressive caching for `/static/`
   - No caching for `/api/`
   - Custom rules for `/` and `/dynamic/` as needed
4. Set up Fastly's WAF rules to protect your endpoints

## Local Testing

To run the server locally:

1. Build the Docker image:
   ```
   docker build -t fastly-test-server .
   ```

2. Run the container:
   ```
   docker run -p 8080:8080 fastly-test-server
   ```

3. Access the server at `http://localhost:8080`

## Monitoring and Logs

- View Cloud Run logs:
  ```
  gcloud run logs read --service fastly-test-server
  ```

- Monitor Cloud Run service:
  ```
  gcloud run services describe fastly-test-server
  ```

## Advanced Fastly Features to Test

1. Edge Dictionaries
2. Edge ACL
3. Custom VCL
4. Shielding
5. Image Optimization
6. Streaming Miss
7. Geolocation

## Performance Testing

1. Load Testing
2. Latency Testing
3. Cache Hit Ratio Optimization

## Security Testing with WAF

1. SQL Injection Protection
2. Cross-Site Scripting (XSS) Protection
3. Remote File Inclusion Protection
4. HTTP Protocol Violations Handling
5. Bot Protection

## Cost Management

While this setup is designed to stay within the free tier, always monitor your GCP billing dashboard to avoid unexpected charges.

## Contributing

Contributions to improve this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For GCP-related issues, refer to [Google Cloud Run Documentation](https://cloud.google.com/run/docs).

For Fastly-related questions, consult [Fastly Documentation](https://docs.fastly.com/) or contact Fastly support.