## Documentation Femhack ComputerWoman - Background Challenge

I have create my program using Python. My program **FemHack.py** calculate ballistic trajectories with a simple CLI. I have divided my program into 3 files: 
- calculator_ballistic_trajectories.py
- create_file.py
- test_femhack.py.

**FemHack.py** is the main file, it welcomes the user and asks if he wants to calculate the information ballistic trajectories. If user doesn’t want, it leaves the program. If user wants to calculate this information, program asks user to introduce the initial velocity (v0) and launch angle (alpha) variables. Finally, it also asks if results want to be saved in a file 

The program always validate the user’s input. Forcing the user to introduce valid string or numbers and re-asking the user in anycase

Then initialize two class imported from two different files: 
- calculator_ballistic_trajectories.py contains class BallisticTrajectories which calculate the ballistic trajectories
- create_file.py which contains class SaveResult where save the result into a json file.

The file **calculator_ballistic_trajectories.py** works with class BallisticTrajectories. In addition to the initialization, it contains two methods:
- cal_h_max, computes the maximum height of the projectile, named as h_max.
- cal_x_max computes the maximum traveled distance, named as x_max, which makes usage of the python math library.

The file **create_file.py** works with class SaveResult that has one method: 
- write_file, defines Key:Value pairs where key is the name to represent each value. Value is the initial velocity (v0), launch angle (alpha), maximum height of the projectile (h_max), maximum traveled distance (x_max)) and write the dictionary in a json file.

Finally, I test each of the class methods in **test_femhack.py**. I’ve used the package unittest.












®Carmen Tur Pérez
MagicGirl
