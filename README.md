# CS-361
1. To request data from the microservice, your program must write a text (alphabetic) value into the recipes.txt file. For example, if in your UI, a user requests a recipe with lemon in the ingredients, write this input "lemon" to recipes.txt as such: inp = input() -> f = open("recipes.txt", "w") -> f.write(inp)
        
2. To recieve data from the microservce, the program must then read the updated text file which will now include the new recipe data. For example: time.sleep(3.0) -> f = open("recipes.txt", "r") -> line = f.readline()
        
3. UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand
