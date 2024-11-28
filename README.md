
## Random Password Generator

This Python script generates secure random passwords with user-specified numbers of letters, symbols, and numbers. It includes both "easy" and "hard" levels of password generation, where the "hard" level shuffles the characters for better security.

### Features:
1. **Customizable Password Composition**:
   - Users specify the number of letters, symbols, and numbers in their password.
   - Example: 5 letters, 3 symbols, and 2 numbers.
   
2. **Two Levels of Password Strength**:
   - **Easy Level**: Characters are added sequentially without shuffling.
   - **Hard Level**: Characters are shuffled for enhanced randomness and security.

3. **Character Pools**:
   - **Letters**: Both uppercase and lowercase letters (a-z, A-Z).
   - **Symbols**: Special characters (`!`, `@`, `#`, etc.).
   - **Numbers**: Digits (`0-9`).

### How It Works:
1. The script prompts the user to input the desired count of:
   - Letters
   - Symbols
   - Numbers
2. Characters are randomly chosen from their respective pools.
3. In the "hard" level:
   - All characters are stored in a list.
   - The list is shuffled to randomize the order.
   - The shuffled list is converted into a string to create the final password.

### Example Usage:
```plaintext
Welcome to Random Password Generator...
How many letters you wish to have in your password ..:
5
How many symbols you wish to have in your password ..:
3
How many numbers you wish to have in your password ..:
2
Your generated password is: a$T&9Bc4!
```

### Implementation Details:
- **Easy Level**: (Commented out in the code)
  - Sequentially appends characters to the password string.
  - Suitable for simple use cases, but less secure.
  
- **Hard Level**:
  - Appends characters to a list, shuffles them, and then converts the list into a string.
  - Ensures high randomness and is recommended for secure password generation.

### Code Structure:
- `letters`: A list of uppercase and lowercase letters.
- `symbols`: A list of commonly used special characters.
- `numbers`: A list of digits from 0 to 9.
- Functions:
  - Randomly select characters using `random.choice`.
  - Shuffle the final password list using `random.shuffle`.

### Security Note:
Always use the hard-level shuffled passwords for better security against brute force or pattern-based attacks.

 
 
