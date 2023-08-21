import random
import time

OPERATORS = ["+", "-", "*"]
MIN_VAL = 1
MAX_VAL = 20
NUM_PROBLEMS = 10

def generate_problem():
    num1 = random.randint(MIN_VAL, MAX_VAL)
    num2 = random.randint(MIN_VAL, MAX_VAL)
    operation = random.choice(OPERATORS)
    expr = str(num1) + " " + operation + " " + str(num2)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(NUM_PROBLEMS):
    expr, answer = generate_problem()
    guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
    if guess != str(answer):
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------")
print("Time:", total_time, "seconds!")
print("Score:", NUM_PROBLEMS-wrong, "/", NUM_PROBLEMS)