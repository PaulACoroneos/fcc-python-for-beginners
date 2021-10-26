import random

feet_in_mile = 5280
family = ["Paul", "Peter", "Katerina", " Pam"]

def get_file_ext(filename):
  return filename[filename.index(".") + 1:]

def roll_dice(num):
  return random.randint(0,num)
