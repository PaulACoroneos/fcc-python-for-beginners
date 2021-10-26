question_prompts = [
  "What colors are apples?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
  "What colors are bananas?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
  "What colors are eggplants?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n"
]

class Question:
  def __init__(self,prompt,answer):
    self.prompt = prompt
    self.answer = answer


questions = [
  Question(question_prompts[0],"a"),
  Question(question_prompts[1],"c"),
  Question(question_prompts[2],"b")
]

def run_test(questions):
  score = 0
  for question in questions:
    response = input(question.prompt)
    if response == question.answer:
      print("You were correct!\n")
      score += 1
    else:
      print("Sorry the answer was " + question.answer + "\n")

  print("You got " + str(score) + " question(s) correct!\n")


run_test(questions)