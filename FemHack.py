from calculator_ballistic_trajectories import BallisticTrajectories
from create_file import SaveResult

# Welcome to user.
print('\nHi! Do you want to calculate quickly the '
      'information ballistic trajectories?(y/n) ')

while True:
    hello = input(' ')
    if hello == 'y':
        break
    elif hello == 'n':
        print('Sorry to hear that. Have a nice day, Bye!')
        quit()
    else:
        print("Sorry, I didn't understand you."
              "\nDo you want to calculate quickly the "
              "information ballistic trajectories?(y/n) ")

# Get the data to INITIAL VELOCITY and LAUNCH ANGLE.
v0 = ""
alpha = ""

print('\nEnter value for Initial Velocity and press enter\n')

while True:
    v0 = input(' ')
    try:
        v0 = float(v0)
        break
    except ValueError:
        print("I can't work with this data.\n"
              "Enter value for Initial Velocity, REMEMBER IS A NUMBER!,\n"
              "and press enter")


print('\nEnter value for Launch Angle and press enter\n')

while True:
    alpha = input(' ')
    try:
        alpha = float(alpha)
        if 0 <= float(alpha) <= 180:
            break
    except ValueError:
        print("I can't work with this data.\n"
              "Enter value for Launch Angle, REMEMBER IS A NUMBER!,\n"
              "and press enter")

print('\nDo you want to save the results in a file? (y/n)r\n')

while True:
    save_file = input(' ')
    if save_file not in ('y', 'n'):
        print("Sorry, I didn't understand you."
              "\nDo you want to save the results "
              "in a file? (y/n) ")
    else:
        break


# Calculate the ballistic trajectories with programs that we have import.
ballistic_tra = BallisticTrajectories(v0, alpha)
h_max = ballistic_tra.cal_h_max()
x_max = ballistic_tra.cal_x_max()
print("Calculating...")
print(f"The maximum height of the projectile is {h_max}")
print(f"The maximum traveled distance is {x_max}")

# Save the result into a json file.
if save_file =='y':
    print("Saving file in computerwomen.json...")
    save_result = SaveResult(v0, alpha, h_max, x_max)
    save_result.write_file("computerwomen.json")

print("thanks, good bye!!")
exit()