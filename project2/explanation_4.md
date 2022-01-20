#Explanation of Approach
The nested group class structure lends itself to a recursion. Each layer deserves the same searching approach, since a user can be in a group if its in the users list or in the subgroups contained within the group. I also knew I was going to have to deal with making the O(n) list lookups faster. Originally, I implemented the recursive solution with lookups in each call, which resulted in a polynomial O(n)^m solution where m is the number of nested subgroups. Since for each nested subgroup there was an O(n) lookup. Instead of taking this approach, I use the recursive function to collect all the subgroups together in a list. The group in each list is then iterated through to get all the users and eventually perform a lookup for the target user.

#Time complexity
The time complexity of my solution is O(n). Iterating through the subgroups in each recursive call does take some time but in the limit of high n (a high number of users) this time is negligible. This is because the number of users will be much greater than then number of groups/subgroups in a particular group class instance. After the recursive calls, the users are retrieved and an O(n) lookup is performed to check if the target user is in the users list.

#Space complexity
The space complexity of my solution is O(n) since we create a list of all the users. We also create a list of all the subgroups, but this space is negligible in the limit as the number of users goes to infinity.
