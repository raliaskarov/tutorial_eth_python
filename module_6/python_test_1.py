# >> Open the task description on the right-hand side under "Task" 
# >> You can enlarge this window by clicking on the blue arrow at the top right.

# Define an input

while True:
  isPalindrome = True
  
  input_text = input("Input word: ")
  len_input = len(input_text)
  for i in range (len_input):
    j = len_input - i -1 
    i_char = input_text[i]
    j_char = input_text[j]
    print(f"Symbol {i}: {i_char} vs symbol {j}: {j_char}")
    if i_char != j_char:
      isPalindrome = False
  # Define a program that checks whether a given word is a palindrome. 
  # Set the Boolean variable "isPalindrome" accordingly.
  
  
  # This print statement should *not* be removed.
  print("Palindrome:", isPalindrome)
