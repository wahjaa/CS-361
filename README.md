# CS-361
1. To request data from the microservice, your program must write a text (alphabetic) value into the recipes.txt file. For example, if in your UI, a user requests a recipe with lemon in the ingredients, write this input "lemon" to recipes.txt as such: inp = input() -> f = open("recipes.txt", "w") -> f.write(inp)
        
2. To recieve data from the microservce, the program must then read the updated text file which will now include the new recipe data. For example: time.sleep(3.0) -> f = open("recipes.txt", "r") -> line = f.readline()
        
3. UML sequence diagram <img width="663" alt="Screen Shot 2023-02-13 at 12 54 35 PM" src="https://user-images.githubusercontent.com/97059544/218561182-47234d9a-2e90-42b2-9ebd-ae50f0441a84.png">

