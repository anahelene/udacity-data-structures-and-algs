#Explanation of Approach
I created a helper function to take care of the recursive search. This helper function calls itself, and modifies the input, path_name, with each call. The base case occurs when the end of a path is reached (a file is reached) and the list_of_paths is returned. The list of paths is built upon over each recursive call, as it's initialized in the main function and passed into each call of the helper function.

#Time complexity
The time complexity of this solution is O(n) where n is the number of items underneath the path. For each item we have to concatenate it with its path and check the suffix. The path name is then added to the list of paths if the item ends with the suffix, and if not a recursive call is made and the process begins again. The number of operations is proportional to the number of items underneath the path, so we have a linear time complexity.

#Space complexity
The space complexity is O(n) where n is the maximum depth of the file structure. In the worst case, the files with the desired suffix will be located at the maximum depth of the file structure. So the call stack will contain each of the previous function calls and the each of the previous states of the list of paths.
