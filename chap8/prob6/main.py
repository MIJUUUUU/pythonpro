import random

def trivia_game():
    questions_and_choices_and_explanations = {
        " What is the largest cat breed in the world?": {
            "choices": ["1-  Siamese", "2- Lion", "3- Bengal", "4- Maine Coon"],
            "correct_choice": "2",
            "explanation": " Lions belong to the big cat family and are one of the largest cat breeds in terms of weight and size."
        },
        " What is one of the classic toppings for pizza?": {
            "choices": ["1- Olives", "2- Mushrooms", "3- Pineapple", "4- Pepperoni"],
            "correct_choice": "4",
            "explanation": " Pepperoni is a popular pizza topping, known as thinly sliced sausage."
        },
        "Where is the highest mountain on Earth located?": {
            "choices": ["1- Alps", "2- Andes", "3-  Everest", "4- Kilimanjaro"],
            "correct_choice": "3",
            "explanation": "Mount Everest is part of the Himalayan mountain range and is known as the highest mountain on Earth."
        },
        "Who is the protagonist of the 'Harry Potter' series?": {
            "choices": ["1-  Harry Potter", "2- Hermione Granger", "3- Draco Malfoy", "4- Ron Weasley"],
            "correct_choice": "1",
            "explanation": "Harry Potter is the main character in J.K. Rowling's novel series about a wizard's adventures."
        },
        " Which animal can extend its nose above water to breathe?": {
            "choices": ["1- Penguin", "2-. Dolphin", "3-  Alligator", "4- Turtle"],
            "correct_choice": "3",
            "explanation": " Alligators are known for their ability to extend their noses above water to breathe, a unique feature among animals."
        },
        "Which season is characterized by colder temperatures and often includes snowfall?": {
            "choices": ["1- Winter", "2- Spring", "3- Summer", "4- Autumn"],
            "correct_choice": "1",
            "explanation": "Winter is the season associated with colder temperatures and, in many regions, snowfall."
        },
        " Which of the following animals is known for its ability to fly?": {
            "choices": ["1- Elephant", "2- Kangaroo", "3-  Dolphin", "4- Eagle"],
            "correct_choice": "4",
            "explanation": "Eagles are birds of prey known for their impressive flying abilities."
        },
        "What is the chemical symbol for gold?": {
            "choices": ["1- Ag", "2- Au", "3- Fe", "4- Cu"],
            "correct_choice": "2",
            "explanation": "The chemical symbol for gold is Au."
        }
    }

    question = random.choice(list(questions_and_choices_and_explanations.keys()))

    print(f"\nQuestion: {question}")
    for choice in questions_and_choices_and_explanations[question]["choices"]:
        print(choice)

    user_answer = input("Your Answer (Enter the letter of your choice): ")

    correct_choice = questions_and_choices_and_explanations[question]["correct_choice"]
    explanation = questions_and_choices_and_explanations[question]["explanation"]
    
    if user_answer.upper() == correct_choice:
        print(f"Correct! {explanation}\n")
    else:
        print(f"Wrong! The correct answer is: {correct_choice}. {explanation}\n")

if __name__ == "__main__":
    for _ in range(8):
        trivia_game()
