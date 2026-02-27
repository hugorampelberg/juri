# Juri

## Tech Stack
- **Backend:** Python with FastAPI
- **Frontend:** Next.js

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Node.js 14 or higher

### Backend Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/hugorampelberg/juri.git
   cd juri/backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. **Navigate to the frontend directory:**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the Next.js development server:**
   ```bash
   npm run dev
   ```