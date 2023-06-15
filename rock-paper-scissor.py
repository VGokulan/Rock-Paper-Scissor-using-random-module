import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

p=[rock,paper,scissor]

d=random.choice(p)
print('''
rock paper scissor
    
choose option
'1.rock'
'2.paper'
'3.scissor'
''')
ch=int(input("Enter choice: "))
print(f"your choice:\n{p[ch-1]}")
print(f"computer choice:\n {d}")

if p[ch-1]==d:
    print("draw")
elif(p[ch-1] == rock and d == paper) or (p[ch-1] == paper and d == scissor) or (p[ch-1] == scissor and d == rock):
    print("you lose")
else:
    print("you win")