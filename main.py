import random
import time
from pathlib import Path
import gui
s=0
with open ((Path(__file__).parent / "highscore.txt").resolve(), "r") as f:
    highscore=f.read()

while True:

   # s is score

    a = random.randint(0, 100)

    b = random.randint(0, 100)
    print(b,"*", a)
    num = a * b


    d = int(input())

    if d == num:
        s=s+1
        print("correct")
        time.sleep(1)
        print ("Your current score is:",s)
        time.sleep(1)
        continue
    else:
        print("Game Over")
        print("the correct answer is:" , num)
        time.sleep(1)
        if s > int(highscore):
                highscore=s
                print("new highscore:",s)
                with open ("highscore.txt", "w") as f:
                    f.write(str(highscore))
        else:
                print("Highscore", highscore)
                print("your score:", s)
                time.sleep(3)

    break




