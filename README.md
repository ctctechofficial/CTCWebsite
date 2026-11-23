# CTC Tech — CodeToCareer (FastAPI)

Responsive static-style landing website served by a FastAPI backend.

## Run locally
1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend:
   ```bash
   python app.py
   ```
   Or:
   ```bash
   uvicorn app:app --reload
   ```
5. Open the website: http://127.0.0.1:8000
6. API health check: http://127.0.0.1:8000/api/health
7. FastAPI docs: http://127.0.0.1:8000/docs

## Structure
- `app.py`: FastAPI backend and website route
- `templates/index.html`: website HTML
- `static/style.css`: styling
- `static/script.js`: client-side menu behavior
- `static/robots.txt` and `static/sitemap.xml`: SEO starter files

## Before publishing
Replace `YOUR-DOMAIN-HERE` in the HTML and SEO files with your domain, and update the contact email to the business email you actually use. Deploy to a Python hosting service, then submit your domain in Google Search Console.
