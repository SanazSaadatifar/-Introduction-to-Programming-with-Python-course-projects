# Homework 5 - Herpetology 🦎🐍🐊🐢🐸
Homework 5 practice on dicts, sets, and strings

Data for this assignment comes from the Society for the Study of Amphibians and Reptiles (SSAR) [ssarherps.org](https://ssarherps.org/). Documentation for this dataset can be found on [GitHub](https://github.com/SSARHERPS/SSAR-species-database) if you are curious. The complete dataset includes many other fields that have been removed for simplicity.

In short, your program will allow the user to query data from SSAR. An example of what your final result might look like is given below. The parts marked in <span style="color:red">red</span> are user input.
![Example Output](example_screenshot.png)

## Part 1 - Instructions
This assignment is meant to ensure that you:
* Can manipulate real data and user input
* Understand `dict`, `set`, and `str`
* Gain experience accessing and searching through keys
* Implement and call user-defined functions
* Become familiar with the string functions

You will complete the functions in [hw5_herpetology.py](hw5_herpetology.py) to:

1. Define a function called `csvToDictOfLists` which accepts a file name as a parameter and then returns a dictionary of lists. This dictionary should contain the contents of the given file with the first element as the key and the rest of the comma seperated values stored as a list of strings linked to the key. The first line of the file (the headers) should not be included in the returned dictionary.

2. Define a function called `filterKeys` which accepts a dictionary as described in Step 1 and a string to filter against. It should then return a list of keys which coincide with the given string.

3. Define a function called `columnToSet` which accepts a dictionary as described in Step 1 and a column index then returns a set which contains all of the values from that column index. For example, if the index was zero then append all of the zeroth elements from the dictionary to the returned list.

4. Define a function called `filterByColumn` which accepts a dictionary as described in Step 1, a column index (similar to Step 3), and a string value. Then return a list of keys which have a column element that matches against the given string.

Then complete `main` so that the program interacts with the user to:
0. Read the data from the given comma separated value file.
1. Present the user with options for animals to list by `Genus`, `Species`, `Subspecies`, or `Type`. The user does not have to select any of these categories and can instead go on to Step 3.
2. Provide the user with all available options from the category they selected with duplicates removed. The user should then identify how they want to filter the reptiles and amphibians.
3. Search through the data to find all of the animals that could match the user's request then display them. In the event that only one animal matches the criteria, present all of the information associated with that animal. Should no animals match the criteria, then let the user know.
4. Ask the user if they wish to restart. In the event that they do, go to Step 1. Otherwise gracefully end the program.

See the screenshot given earlier for an example of this process in action. Your program does not need to look exactly like the screenshot.
 
 This lab assignment assumes input from the user and files. To ensure that GitHub can test and run your code, ***do not*** specify the entire path to the data file. Also add any regular keyboard input to the [keyboard_input.txt](keyboard_input.txt) file.

 ## Part 2 - Reflection
 Update the README to answer the following questions:

 1. Add a screenshot (or screenshots) here demonstrating how your program interacts with the user to display results. ![Example Output](Sanaz.PNG)
 2. Describe two important differences between a `set` and a `list`. 1) Set does not accept duplicates of its items; however, in List we can duplicates of different types. 2) A list is ordered meaning individual elements in a list can be referred to using an index, however, Set is not ordered, and it is not possible to refer to individual elements using an index.
 3. Explain dictionary's `keys()` and `values()` functions. Dictionaries consists for Keys and Values which can be considered as attributes of keys as they refer to a key. keys() Returns a list containing the dictionary's keys, and values() Returns a list of all the values in the dictionary. 
 4. What strategy did you use to ensure that your program worked even if the input capitalization did not match? I used str.lower() for both the user inputs and also whatever is imported from CSV file so any function that would check these matches, does not even get capital letters, so matches are done with lowers only.  
 5. Were there any names from the data that you found particularly interesting? Yes some animals with different colors for different parts of their body was interesting to me such as Texas Yellow-Headed Racerunner, Yellow-Headed Gecko, Mexican Black-Headed Snake, and, Trans-Pecos Black-Headed Snake. 

 ---
 ## Running Tests Locally
 You do not have to wait for test results from GitHub because you can run tests on your own computer. The tester uses the program `pytest` which can be installed using the command `pip install -U pytest` (more info available at [https://docs.pytest.org](https://docs.pytest.org/en/stable/getting-started.html)). Use the following command to run `pytest`.

 ``` bash
 pytest
 ```
