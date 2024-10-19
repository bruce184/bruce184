from playsound import playsound 
import time 

# playsound('alarm sound.mp3')

# Just remember these 
clear = '\033[2J'
clear_and_return = '\033[H'

def alarm(seconds):
    time_elapsed = 0

    print(clear)
    while time_elapsed <seconds: 
        time.slepp(1) 
        time_elapsed += 1

        time_left = seconds - time_elapsed 
        minute_left = time_left // 60     # 125//60 = 2
        second_left = time_left % 60  

        # to make the display empty, just has the timer
        print(f'{clear_and_return} Alarm will sound in: {minute_left: 02d}:{second_left: 02d}') # 02d: to make 2 digits
        
    playsound('alarm sound.mp3')

min = int(input('How many minutes to wait: '))
sec = int(input('How many seconds to wait: '))
total_seconds = min * 60 + sec # calculate the total seconds to countdown
alarm(total_seconds)

