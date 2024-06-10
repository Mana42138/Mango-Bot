# -*- coding: utf-8 -*-

import os
import string
import base64
import math

import discord
from discord import app_commands
from discord.ext import commands

symboles = 'qwertyuiopasdfghjklzxcvbnm*^`<&/?-<>!~$%{'
replace = f"{string.ascii_lowercase}1234567890#!=[]"

class Obf():
    def __init__(self, data) -> None:
        self.data = data
        self.replace = list(replace)  # ['a', 'b', 'c', ..., 'z']
        self.symbols = list(symboles)
        self.obfuscated = self.replace_characters()
        
    def oneline(self, square_code):
        # Split the square code into lines
        lines = square_code.split('\n')
        # Remove empty lines and trailing whitespace
        lines = [line.strip() for line in lines if line.strip()]
        # Concatenate all lines into a single string
        code = 'JKLXYZP'.join(lines)
        return code
        
    def replace_characters(self):
        """
        Replace each character in the data with corresponding symbols from the symbols list.
    
        :return: str, data with replaced symbols
        """
        replace_to_symbol = dict(zip(self.replace, self.symbols))
        return self.oneline(''.join(replace_to_symbol.get(char, char) for char in self.data))

class Deobf():
    def __init__(self, data) -> None:
        self.data = data
        self.replace = list(replace)  # ['a', 'b', 'c', ..., 'z']
        self.symbols = list(symboles)
        self.deobfuscated = self.replace_characters()
        
    def replace_80(self, data):
        replaced_data = ""
        i = 0
        while i < len(data):
            # Check if the current character and the next one form the number 80
            if i < len(data) - 1 and data[i] == "8" and data[i + 1] == "0":
                replaced_data += "->"
                i += 2  # Skip the next character since it's already part of the number 80
            else:
                replaced_data += data[i]
                i += 1
        return replaced_data
    
    def reverse_oneline(self, code):
        # Split the code into lines based on the specified characters
        lines = code.split('JKLXYZP')

        # Concatenate lines into a single string with line breaks
        code = '\n'.join(lines)

        return code
    
    def reformat_code(self, code):
        # Split the code into lines
        lines = code.split('\n')
        # Initialize variables to keep track of the indentation level and class/function definition status
        current_indentation = 0
        in_class_or_function = False

        for i, line in enumerate(lines):
            # Count the indentation spaces
            indentation = len(line) - len(line.lstrip())

            # Check if a class or function definition starts
            if line.strip().startswith(("class", "def ")):
                in_class_or_function = True
                current_indentation = indentation // 4  # Set the current indentation level based on the class/function's indentation
            elif line.strip() == "":
                # Skip empty lines
                continue
            elif in_class_or_function:
                # If inside a class or function, adjust the indentation
                current_indentation += 1
                in_class_or_function = False

            # Adjust the indentation of the line
            lines[i] = " " * (4 * current_indentation) + line.lstrip()

        # Reconstruct the code with proper indentation
        formatted_code = "\n".join(lines)
        return formatted_code

    def replace_characters(self):
        """
        Replace each symbol in the data with corresponding characters from the replace list.
    
        :return: str, data with replaced characters
        """
        replace_to_symbol = dict(zip(self.symbols, self.replace))
        return self.replace_80(self.reformat_code(self.reverse_oneline(''.join(replace_to_symbol.get(char, char) for char in self.data))))

# Example usage
input_data = '''
class Obfuscat:
    def __init__(self, data) -> None:
        self.data = data
        self.replace = list(string.ascii_lowercase)  # ['a', 'b', 'c', ..., 'z']
        self.symbols = list('qwertyuiopasdfghjklzxcvbnm')
        self.obfuscated = self.replace_characters()
        1.5
    def replace_characters(self):
        """
        Replace x with y
        Replace each character in the data with corresponding symbols from the symbols list.
    
        :return: str, data with replaced symbols
        """
        replace_to_symbol = dict(zip(self.replace, self.symbols))
        return ''.join(replace_to_symbol.get(char, char) for char in self.data)
'''

async def Obfuscate(file: discord.Attachment) -> discord.File:
    try:
        file_extension = os.path.splitext(file.filename)[1][1:]
        print(f"File extension: {file_extension}")
        print("File supported!")

        file_content = await file.read()

        obfuscated_content = Obf(file_content.decode())
        
        obfuscated_file_path = f"{os.path.splitext(os.path.basename(file.filename))[0]}-obfuscated.{file_extension}"
        with open(obfuscated_file_path, "w") as obfuscated_file:
            obfuscated_file.write(obfuscated_content.obfuscated)
        
        return discord.File(obfuscated_file_path)

    except Exception as e:
        print(f"An error occurred during obfuscation: {e}")
        raise  # Re-raise the exception to propagate it upwards
    

async def DeObfuscate(file: discord.Attachment) -> discord.File:
    try:
        file_extension = os.path.splitext(file.filename)[1][1:]
        print(f"File extension: {file_extension}")
        print("File supported!")

        file_content = await file.read()

        obfuscated_content = Deobf(file_content.decode())
        
        obfuscated_file_path = f"{os.path.splitext(os.path.basename(file.filename))[0]}-deobfuscated.{file_extension}"
        with open(obfuscated_file_path, "w") as obfuscated_file:
            obfuscated_file.write(obfuscated_content.deobfuscated)
        
        return discord.File(obfuscated_file_path)

    except Exception as e:
        print(f"An error occurred during obfuscation: {e}")
        raise  # Re-raise the exception to propagate it upwards

