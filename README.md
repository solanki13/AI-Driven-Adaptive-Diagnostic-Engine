# AI-Driven Adaptive Diagnostic Engine

## Overview
This project implements a 1-Dimensional Adaptive Testing System that dynamically adjusts question difficulty based on a student's responses. The system estimates the student's ability level and selects questions accordingly.

The objective is to create a smarter assessment platform that adapts question difficulty in real time and generates personalized study recommendations using AI.

The system uses MongoDB for storing GRE-style questions, FastAPI for backend APIs, and OpenAI API for generating study plans.

------------------------------------------------------------

## Tech Stack

Programming Language: Python  
Backend Framework: FastAPI  
Database: MongoDB  
AI Integration: OpenAI API  
API Documentation: FastAPI Swagger UI  

------------------------------------------------------------

## Project Structure

AI-Driven-Adaptive-Diagnostic-Engine
│
├── app
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── adaptive_engine.py
│   └── ai_plan.py
│
├── seed_questions.py
├── requirements.txt
├── README.md
├── .gitignore

------------------------------------------------------------

## How to Run the Project

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Start MongoDB server

Make sure MongoDB is running locally on port 27017.

Step 3: Seed questions into the database

python seed_questions.py

Step 4: Run the FastAPI server

uvicorn app.main:app --reload

Step 5: Open API documentation

http://127.0.0.1:8000/docs

------------------------------------------------------------

## Adaptive Algorithm Logic

The system uses a simplified adaptive testing algorithm inspired by Item Response Theory (IRT).

Algorithm Steps:

1. Each student session starts with an ability score of 0.5.
2. The system selects a question with difficulty close to the student’s ability.
3. If the student answers correctly, the ability score increases.
4. If the student answers incorrectly, the ability score decreases.
5. Ability values are constrained between 0.1 and 1.0.
6. The next question is selected using the updated ability score.

Example Logic:

If correct:
ability = ability + 0.1

If incorrect:
ability = ability - 0.1

This allows the system to dynamically adjust question difficulty.

------------------------------------------------------------

## AI Integration

After the test is completed, the system analyzes the student's performance and sends weak topic information to the OpenAI API.

The AI then generates a 3-step personalized study plan to help the student improve.

Example Study Plan:

1. Review algebra fundamentals including linear equations.
2. Practice GRE-style probability problems daily.
3. Take a timed mock test to evaluate progress.

If the OpenAI API is unavailable due to quota limitations, the system provides a fallback rule-based study plan.

------------------------------------------------------------

## API Documentation

POST /start-session  
Starts a new testing session and initializes ability score.

GET /next-question  
Returns the next question based on student ability.

POST /submit-answer  
Checks the answer and updates ability score.

POST /study-plan  
Generates an AI-based personalized study plan.

------------------------------------------------------------

## Database Schema

Questions Collection Example:

{
question: "Solve: 3x = 12",
options: ["2","3","4","5"],
correct_answer: "4",
difficulty: 0.3,
topic: "Algebra"
}

User Session Example:

{
user_id: "student1",
ability: 0.5,
score: 0
}

------------------------------------------------------------

## AI Log

AI tools such as ChatGPT were used during development to assist with:

• Designing the adaptive testing algorithm  
• Structuring the FastAPI backend architecture  
• Implementing MongoDB schema and queries  
• Integrating OpenAI API for generating study plans  
• Generating GRE-style questions for the dataset  

### Challenges

One challenge encountered was OpenAI API quota limitations during testing.  
To ensure the system continues functioning, a fallback study plan generator was implemented.

------------------------------------------------------------

## Conclusion

This project demonstrates how adaptive testing systems can improve assessments by dynamically adjusting difficulty levels and providing AI-powered learning recommendations.# AI-Driven-Adaptive-Diagnostic-Engine