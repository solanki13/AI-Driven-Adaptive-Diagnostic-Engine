from app.database import questions_collection

questions = [

{
"question": "2 + 2 = ?",
"options": ["3","4","5","6"],
"correct_answer": "4",
"difficulty": 0.1,
"topic": "Arithmetic"
},

{
"question": "5 × 6 = ?",
"options": ["25","30","35","40"],
"correct_answer": "30",
"difficulty": 0.2,
"topic": "Arithmetic"
},

{
"question": "Solve: 3x = 12",
"options": ["2","3","4","5"],
"correct_answer": "4",
"difficulty": 0.3,
"topic": "Algebra"
},

{
"question": "Solve: 2x + 5 = 15",
"options": ["3","5","10","15"],
"correct_answer": "5",
"difficulty": 0.4,
"topic": "Algebra"
},

{
"question": "What is 7² ?",
"options": ["42","48","49","56"],
"correct_answer": "49",
"difficulty": 0.3,
"topic": "Arithmetic"
},

{
"question": "Derivative of x² ?",
"options": ["x","2x","x²","2"],
"correct_answer": "2x",
"difficulty": 0.7,
"topic": "Calculus"
},

{
"question": "What is √81 ?",
"options": ["7","8","9","10"],
"correct_answer": "9",
"difficulty": 0.2,
"topic": "Arithmetic"
},

{
"question": "Solve: x² = 16",
"options": ["2","4","6","8"],
"correct_answer": "4",
"difficulty": 0.4,
"topic": "Algebra"
},

{
"question": "10% of 200 is?",
"options": ["10","20","30","40"],
"correct_answer": "20",
"difficulty": 0.3,
"topic": "Arithmetic"
},

{
"question": "What is 15² ?",
"options": ["200","215","225","250"],
"correct_answer": "225",
"difficulty": 0.4,
"topic": "Arithmetic"
},

{
"question": "Solve: 4x + 8 = 24",
"options": ["2","3","4","5"],
"correct_answer": "4",
"difficulty": 0.5,
"topic": "Algebra"
},

{
"question": "What is log10(100)?",
"options": ["1","2","3","4"],
"correct_answer": "2",
"difficulty": 0.6,
"topic": "Logarithms"
},

{
"question": "Derivative of sin(x)?",
"options": ["cos(x)","sin(x)","tan(x)","-sin(x)"],
"correct_answer": "cos(x)",
"difficulty": 0.7,
"topic": "Calculus"
},

{
"question": "What is 8 × 7 ?",
"options": ["54","56","58","60"],
"correct_answer": "56",
"difficulty": 0.2,
"topic": "Arithmetic"
},

{
"question": "Solve: 5x = 45",
"options": ["5","7","9","11"],
"correct_answer": "9",
"difficulty": 0.3,
"topic": "Algebra"
},

{
"question": "What is 12² ?",
"options": ["124","134","144","154"],
"correct_answer": "144",
"difficulty": 0.3,
"topic": "Arithmetic"
},

{
"question": "Integral of x dx?",
"options": ["x²/2","2x","x²","1/x"],
"correct_answer": "x²/2",
"difficulty": 0.8,
"topic": "Calculus"
},

{
"question": "What is 50% of 80?",
"options": ["20","30","40","50"],
"correct_answer": "40",
"difficulty": 0.2,
"topic": "Arithmetic"
},

{
"question": "Solve: x/4 = 5",
"options": ["10","15","20","25"],
"correct_answer": "20",
"difficulty": 0.4,
"topic": "Algebra"
},

{
"question": "What is 9 × 9 ?",
"options": ["72","80","81","90"],
"correct_answer": "81",
"difficulty": 0.2,
"topic": "Arithmetic"
}

]

questions_collection.insert_many(questions)

print("Questions inserted successfully")