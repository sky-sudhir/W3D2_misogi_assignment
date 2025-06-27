# Multimodal QA Agent

A web application that allows users to upload images and ask questions about them using Google's Gemini 2.0 Flash model.

## Features

- Upload images via file selection
- Ask natural language questions about the uploaded images
- Get AI-powered responses about the image content
- Responsive design that works on both desktop and mobile
- Modern UI built with Next.js, shadcn/ui, and Tailwind CSS

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui
- React Hook Form

### Backend
- FastAPI
- Google's Gemini 2.0 Flash model
- Python 3.x

## Prerequisites

- Node.js 18+ and npm/yarn/pnpm
- Python 3.8+
- Google API key with access to Gemini API

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## API Endpoints

### POST /ask

Analyzes an image and answers questions about it.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body:
  - `image`: The image file
  - `question`: The question about the image

**Response:**
```json
{
  "answer": "The AI's response to your question",
  "used_model": "gemini-2.0-flash"
}
```

## Environment Variables

### Backend
- `GOOGLE_API_KEY`: Your Google API key with access to Gemini API

## Project Structure

```
.
├── backend/               # FastAPI backend
│   ├── main.py            # Main application file
│   ├── requirements.txt   # Python dependencies
│   └── .env              # Environment variables
├── frontend/              # Next.js frontend
│   ├── src/
│   │   ├── app/         # Next.js app directory
│   │   └── components/    # React components
│   ├── public/            # Static files
│   └── package.json       # Node.js dependencies
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Google Gemini API](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Next.js](https://nextjs.org/)
- [shadcn/ui](https://ui.shadcn.com/)
