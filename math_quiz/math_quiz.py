import random

def generate_random_number(minimum: int = 1, maximum: int = 10) -> int:
    """
    Generate a random integer between minimum and maximum values.
    
    Args:
        minimum (int): Lower bound for random number (default: 1)
        maximum (int): Upper bound for random number (default: 10)
    
    Returns:
        int: A random number between minimum and maximum (inclusive)
    """
    # Ensure we get an integer within specified range
    return random.randint(minimum, maximum)


def select_operator() -> str:
    """
    Select a random mathematical operator.
    
    Returns:
        str: One of three mathematical operators: '+', '-', or '*'
    """
    # List of available operators for the quiz
    operators = ['+', '-', '*']
    return random.choice(operators)


def create_math_problem(number1: int, number2: int, operator: str) -> tuple[str, int]:
    """
    Create a mathematical problem and calculate its correct answer.
    
    Args:
        number1 (int): First number in the problem
        number2 (int): Second number in the problem
        operator (str): Mathematical operator ('+', '-', or '*')
    
    Returns:
        tuple[str, int]: A tuple containing (problem_string, correct_answer)
    """
    # Format the problem string
    problem = f"{number1} {operator} {number2}"
    
    # Calculate the correct answer based on the operator
    # Bug fix: Previous version had incorrect operations
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:  # operator must be '*'
        answer = number1 * number2
        
    return problem, answer


def get_user_input(prompt: str) -> int:
    """
    Get and validate numerical input from the user.
    
    Args:
        prompt (str): The prompt to display to the user
    
    Returns:
        int: The validated integer input from the user
    
    Raises:
        ValueError: If the input cannot be converted to an integer
    """
    while True:
        try:
            # Get user input and convert to integer
            user_answer = int(input(prompt))
            return user_answer
        except ValueError:
            # Handle invalid input (non-numeric)
            print("Error: Please enter a valid number!")
            continue


def math_quiz() -> None:
    """
    Run an interactive math quiz game.
    
    The quiz presents the user with mathematical problems and keeps track of their score.
    Each correct answer awards one point. The game continues for a fixed number of questions.
    """
    # Initialize game variables
    score = 0
    total_questions = 3  # Bug fix: Changed from 3.14159... to 3 (needs to be integer)
    
    # Display welcome message
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Main game loop
    for question_number in range(1, total_questions + 1):
        try:
            # Generate random numbers for the problem
            # Bug fix: Changed second number range from 5.5 to 5 (needs to be integer)
            number1 = generate_random_number(1, 10)
            number2 = generate_random_number(1, 5)
            operator = select_operator()

            # Create the problem and get correct answer
            problem, correct_answer = create_math_problem(number1, number2, operator)
            
            # Display question and get user's answer
            print(f"\nQuestion {question_number}: {problem}")
            
            # Get and validate user input
            user_answer = get_user_input("Your answer: ")
            
            # Check answer and update score
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                # Bug fix: Changed from s += -(-1) to score += 1
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
                
        except Exception as e:
            # Handle any unexpected errors during the game
            print(f"An error occurred: {str(e)}")
            print("Moving to next question...")
            continue

    # Display final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()