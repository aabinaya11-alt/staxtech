quiz_data = {
    1: {
        "question": "What is the capital of France?",
        "options": {
            "A": "London",
            "B": "Berlin",
            "C": "Paris",
            "D": "Madrid"
        },
        "answer": "C"
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Venus",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Saturn"
        },
        "answer": "B"
    },
    3: {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": {
            "A": "Charles Dickens",
            "B": "Mark Twain",
            "C": "William Shakespeare",
            "D": "Jane Austen"
        },
        "answer": "C"
    },
    4: {
        "question": "What is the largest ocean on Earth?",
        "options": {
            "A": "Atlantic Ocean",
            "B": "Indian Ocean",
            "C": "Arctic Ocean",
            "D": "Pacific Ocean"
        },
        "answer": "D"
    },
    5: {
        "question": "In which year did World War II end?",
        "options": {
            "A": "1943",
            "B": "1945",
            "C": "1947",
            "D": "1950"
        },
        "answer": "B"
    }
}

def start_quiz():
    print("=" * 50)
    print("        WELCOME TO THE QUIZ GAME!")
    print("=" * 50)
    print("\nAnswer the following questions by typing A, B, C, or D")
    print("Let's see how much you know!\n")
    
    score = 0
    total_questions = len(quiz_data)
    
    for q_num, q_info in quiz_data.items():
        print(f"Question {q_num}: {q_info['question']}")
        
        for option, text in q_info['options'].items():
            print(f"  {option}. {text}")
        
        user_answer = input("\nYour answer: ").upper()
        
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input! Please enter A, B, C, or D.")
            user_answer = input("Your answer: ").upper()
        
        if user_answer == q_info['answer']:
            print("✓ Correct!\n")
            score += 1
        else:
            correct_option = q_info['answer']
            correct_text = q_info['options'][correct_option]
            print(f"✗ Wrong! The correct answer was {correct_option}. {correct_text}\n")
        
        print("-" * 50)
    
    print("\n" + "=" * 50)
    print("           QUIZ COMPLETED!")
    print("=" * 50)
    print(f"\nYour Score: {score} out of {total_questions}")
    
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 80:
        print("\n🎉 Excellent work! You're a quiz master!")
    elif percentage >= 60:
        print("\n👍 Good job! You know your stuff!")
    elif percentage >= 40:
        print("\n🙂 Not bad! Keep learning!")
    else:
        print("\n📚 Don't worry, practice makes perfect!")
    
    print("\nThanks for playing!\n")

if __name__ == "__main__":
    start_quiz()
