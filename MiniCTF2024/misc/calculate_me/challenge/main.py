from SECRETS import FLAG
import random
import sys, select

def generate_question(optional_value_for_a=None, optional_value_for_b=None):
    a = random.randint(0, 100) if optional_value_for_a is None else optional_value_for_a
    b = random.randint(0, 100) if optional_value_for_b is None else optional_value_for_b
    op = random.choice(['+', '-', '*'])
    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, answer

def main():
    print("Welcome to calculate me!")
    print("I will give you a simple math question, and you have to answer it.")
    print("Let's start!")
    for _ in range(100):
        question, answer = generate_question()
        question, answer = generate_question(question, None)
        print(f"Question: {question}")
        print("Your answer: ", end="")
        sys.stdout.flush()
        user_answer = int(input())
        if user_answer == answer:
            print("Correct!")
        else:
            print("Incorrect!")
            print("Try again next time!")
            return
    print(f"Congratulation! Here is your flag: {FLAG}")

if __name__ == "__main__":
    main()
