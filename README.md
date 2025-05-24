# smart-attendance-tracker

A simple Flask-based web application to manage and track employee attendance via check-ins with timestamp and geolocation. This tool allows users to:

- Add attendance check-ins with employee ID, timestamp, and location coordinates
- View summarized attendance data per employee
- Browse all check-ins across employees
- Search for check-ins nearby a given location within a specified radius

## Features

- Easy-to-use web interface built with Flask and Jinja2 templates
- Data persistence using JSON storage (`data.json`)
- Geolocation distance calculation using Haversine formula for nearby search
- Basic navigation and filtering for attendance records
- Ready to deploy on cloud platforms like Render or Heroku

## Technologies Used

- Python 3.x
- Flask micro-framework
- HTML/Jinja2 templates for frontend
- JSON for simple data storage

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/smart-attendance-tracker.git
cd smart-attendance-tracker
