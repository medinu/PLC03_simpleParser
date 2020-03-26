# **Description**
The purpose of the program is to iterate through a string and systematically categorize the elements into a symbol table. The symbol table includes the actual symbol, token class and its occurance. 

___

## **Logs**
### 3/24/2020
* built most of the individual defs in an outside file to stress test 
* strung everything together in main and parse function
* Note: This could probably be done in a more effective manner because checking if character is special is too time consuming
    * a remedy for this would be to to check for the chars ascii code value

### 3/25/2020
* added check for ascii values rather than scan through the array of special char array 
* optimized the code by removing most if not all variable assignment
* made changes to the addToList function. 

___

# **Sample output**

input: "if [ 123 cat ))) then begin if cat x 12+123 + end] cat [ 12.23, end"

Terminal: 

```
Symbol table:
        symbol:if       category: keyword       occurance: 2
        symbol:[        category: special       occurance: 2
        symbol:123      category: integer       occurance: 2
        symbol:cat      category: identifier    occurance: 3
        symbol:)        category: special       occurance: 3
        symbol:then     category: keyword       occurance: 1
        symbol:begin    category: keyword       occurance: 1
        symbol:x        category: identifier    occurance: 1
        symbol:12       category: integer       occurance: 1
        symbol:+        category: special       occurance: 2
        symbol:end      category: keyword       occurance: 2
        symbol:]        category: special       occurance: 1
        symbol:12.23    category: real          occurance: 1
        symbol:,        category: special       occurance: 1
```