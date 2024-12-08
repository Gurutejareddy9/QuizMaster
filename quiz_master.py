import json
import random

# Load questions from JSON file
def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Generate a quiz with 'n' questions
def generate_quiz(questions, n):
    quiz = random.sample(questions, n)
    return quiz

# Evaluate user responses
def grade_quiz(quiz, user_responses):
    score = 0
    for i, question in enumerate(quiz):
        if user_responses[i].lower() == question['answer'].lower():
            score += 1
            print(f"Q{{i+1}}: Correct!")
        else:
            print(f"Q{{i+1}}: Incorrect. The correct answer is {question['answer']}.")
    print(f"\nYour Final Score: {score}/{len(quiz)}")

def main():
    questions = load_questions('questions.json')
    print("Welcome to QuizMaster!")
    num_questions = int(input("How many questions would you like in your quiz? (1-{}): ".format(len(questions))))
    quiz = generate_quiz(questions, num_questions)
    user_responses = []
    
    for i, question in enumerate(quiz):
        print(f"\nQ{i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        response = input("Your Answer: ")
        user_responses.append(response)
    
    grade_quiz(quiz, user_responses)

if __name__ == "__main__":
    main()
