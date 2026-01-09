# Image Upload & Analysis API

A FastAPI service for uploading images and performing mock skin analysis.

## Quick Start

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone/navigate to the project directory:
```bash
cd image_upload
pip install -r requirements.txt
uvicorn app.main:app --reload

The API will be available at http://localhost:8000

Interactive Documentation
Swagger UI: http://localhost:8000/docs

### Available Endpoints
1. Upload Image
POST /api/v1/upload

Upload an image file for analysis.

Request:

Content-Type: multipart/form-data
Body: file (JPEG or PNG, max 5MB)

2. Analyze Image
POST /api/v1/analyze

Perform analysis on a previously uploaded image.

Request:
{
  "image_id": "12345"
}

### Production Improvements
Cloud Storage Integration: Use AWS S3, Azure Blob Storage, or Google Cloud Storage instead of local filesystem

Rate Limiting: Prevent abuse with request throttling

HTTPS Only: Enforce SSL/TLS in production

License
MIT