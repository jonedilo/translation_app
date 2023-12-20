# Multilingual Text Translation App

## Step 1: Sign Up for Google Cloud Translation API

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the "Cloud Translation API" for your project.
4. Create credentials:
   - Choose "Service Account Key."
   - Select "JSON" format.
   - Download the credentials JSON file.

## Step 2: Install Required Libraries

Make sure you have Streamlit and the googletrans library installed. You can install them using the following commands:

```bash
pip install streamlit googletrans==4.0.0-rc1
```

Note: Replace "YOUR_GOOGLE_CREDENTIALS_JSON_FILE.json" with the actual path to your downloaded Google Cloud Translation API credentials file.
