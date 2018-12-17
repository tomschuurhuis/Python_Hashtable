#   1. Import a file with strings
#   2. Let it read through the file and do per string the following:
#       2.1. Break the string up in seperate characters.
#       2.2. The index of the letter in the alphabet will be the power of 2. For example: a = 2^0, b = 2^1, e = 2^5.
#       2.3. Calculate the sum of all characters in the string.
#       2.4. This will be the position/index of the string in a database.

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "1","2","3","4","5","6","7","8","9","0"," "]

f = open("Names.txt","r")
content = f.readlines()
print(content)

for string in range(len(content)):

    character_list = list(content[string])

    for i in range(len(character_list)):
        character = character_list[i]
        for j in range(len(alphabet)):
            if character == alphabet[j]:
