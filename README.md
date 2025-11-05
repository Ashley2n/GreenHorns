# CookQuest - Gamified Cultural Cooking App

A Flask-based web application that transforms cooking into an engaging single-player game. Explore cultural cuisines, complete cooking challenges, and level up your culinary skills.

## 🎯 Features

### MVP Features
- **User Authentication** - Secure registration and login system
- **Cultural Campaigns** - Explore recipes by cultural categories (Italian, Japanese, Mexican, etc.)
- **Single-Player Challenges** - Timer-based cooking sessions with specific recipes
- **Mock AI Grading** - Instant feedback on your culinary creations
- **Progression System** - Earn XP, level up, and unlock achievements
- **Image Upload** - Share photos of your completed dishes

### Technical Features
- Flask web framework with SQLite database
- Responsive web design
- Session-based authentication
- File upload handling
- Progressive enhancement with JavaScript

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   ```
   ```bash
   cd cookquest
    ```
   

### Create virtual environment
```bash
    python -m venv venv
```
- On Windows: venv\Scripts\activate
```bash
    source venv/bin/activate  

```


### Install Dependencies
```bash
    pip install -r requirements.txt
```


### Set up Environment variables
```bash 
  cp .env.example .env
```

### Initialize Database
- Load sample recipes and campaigns
```bash
    flask db init
    flask db migrate
    flask db upgrade
    python seed_data.py  
```

### Run App
- flask run

```bash
python app.py
```

### 📝 API Endpoints

| Method | 	Endpoint | 	Description |
|--------|:---------:|-------------:|
|GET	|/	|Home page - campaign selection|
|GET	|/campaign/<id>|	Recipes for specific campaign|
|GET	|/game/start/<recipe_id>|	Start cooking session|
|POST	|/game/complete|	Submit completed dish|
|GET	|/profile	|User progress and achievements|