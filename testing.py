

import sys
import time


def print_letter_by_letter(sentence, delay=1):
    """
    Prints a sentence letter by letter with a delay between each character.

    :param sentence: The sentence to be printed.
    :param delay: The delay (in seconds) between printing each letter.
    """
    for char in sentence:
        sys.stdout.write(char)  # Print the character without a newline
        sys.stdout.flush()  # Ensure it's immediately written to the terminal
        time.sleep(delay)  # Wait for the specified delay

    print()  # Print a newline after the sentence is fully printed


# Example usage
sentence = "Hello, world! This is just another sentence to see how fast this geos!"
print_letter_by_letter(sentence, delay=0.05)

# def shake_text(text, shakes=10, delay=0.1):
#     for _ in range(shakes):
#         # Move cursor to the beginning of the line
#         sys.stdout.write("\r" + " " * 3 + text)  # Move right
#         sys.stdout.flush()
#         time.sleep(delay)
#
#         sys.stdout.write("\r" + " " * 1 + text)  # Move left
#         sys.stdout.flush()
#         time.sleep(delay)
#
#     # Ensure the text stays visible at the end
#     sys.stdout.write("\r" + text + "\n")
#     sys.stdout.flush()
#
#
# # Example usage
# print("Hello")
# shake_text("Shaking text in Python!")

#
# import time
# import sys
# import shutil
#
#
# def clear_last_three_lines():
#     # Print some lines first to create content
#     print("Line 1: This is the first line.")
#     print("Line 2: This is the second line.")
#     print("Line 3: This is the third line.")
#     print("Line 4: This is the fourth line.")
#     print("Line 5: This is the fifth line.")
#
#     # Wait for a moment to observe the printed lines
#     time.sleep(2)
#
#     # Move the cursor up by 3 lines to the last three lines
#     # Instead of using escape sequences, we simply print blank lines to clear the text
#     for _ in range(3):
#         sys.stdout.write("\033[F")  # Move the cursor up by one line
#
#     # Clear the last 3 lines by overwriting them with spaces
#     terminal_width = shutil.get_terminal_size().columns
#     sys.stdout.write(" " * terminal_width + "\r")  # Clear the first line
#     sys.stdout.write(" " * terminal_width + "\r")  # Clear the second line
#     sys.stdout.write(" " * terminal_width + "\r")  # Clear the third line
#
#     # Optionally, move the cursor back down 3 lines if you need to continue from the same position
#     sys.stdout.write("\033[B\033[B\033[B")  # Move down 3 lines
#
#     # Wait to observe the effect
#     time.sleep(2)
#
#
# # Call the function
# clear_last_three_lines()
# print("hello world")