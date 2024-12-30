questions = [
    {"prompt": "What is the capital of France?", 
     "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], 
     "answer": "A"},
    {"prompt": "Which language is primarily spoken in Brazil?", 
     "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"], 
     "answer": "B"},
    {"prompt": "What is the smallest prime number?", 
     "options": ["A. 1", "B. 2", "C. 3", "D. 5"], 
     "answer": "B"},
    {"prompt": "Who wrote 'To Kill a Mockingbird'?", 
     "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"], 
     "answer": "A"},
    {"prompt": "What is the largest planet in our solar system?", 
     "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Uranus"], 
     "answer": "C"},
    {"prompt": "Which of the following authors wrote 'The Great Gatsby'?",
      "options": ["A. F. Scott Fitzgerald", "B. Ernest Hemingway", "C. Jane Austen", "D. J.K. Rowling"],
      "answer": "A"},
    {"prompt": "What is the chemical symbol for gold?", 
     "options": ["A. Ag", "B. Au", "C. Hg", "D. Pb"], 
     "answer": "B"},
    {"prompt": "Who was the first president of the United States?", 
     "options": ["A. George Washington", "B. Thomas Jefferson", "C. Abraham Lincoln", "D. Franklin D. Roosevelt"], 
     "answer": "A"},
    {"prompt": "What is the largest mammal on Earth?", 
     "options": ["A. Elephant", "B. Blue whale", "C. Hippopotamus", "D. Rhinoceros"], 
     "answer": "B"},
    {"prompt": "Which of the following rivers is the longest in the world?",
      "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"], 
      "answer": "A"},
]

def run_quiz(questions):
    score=0
    for i in questions:
        print(i["prompt"])

        for j in i["options"]:
            print(j)

        ans=input("Enter your answer (A/B/C/D):").upper()

        if ans==(i["answer"]):
            print("Correct Answer!!","\n")
            score+=1

        else:
            print("Wrong!!The correct answer is",i["answer"],"\n")

    print("You got ",score,"out of ",len(questions))

run_quiz(questions)