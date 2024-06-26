# Static Website with Fastly CDN on Google Cloud Platform

This project demonstrates how to host a static website on Google Cloud Platform (GCP) using Cloud Storage, enhanced with Fastly CDN for improved performance and global content delivery.

## Project Overview

This static website showcases the benefits of using Fastly CDN with a GCP-hosted static website. It includes:

- A main page (`index.html`) highlighting Fastly CDN features
- A custom 404 error page (`404.html`)
- Sample images demonstrating CDN benefits

## Prerequisites

- Google Cloud Platform account
- gcloud SDK installed and configured
- Fastly account (for CDN integration)

## Setup Instructions

### 1. Create a GCP Storage Bucket

```bash
gsutil mb gs://cdn1_itsa_house_bucket1
