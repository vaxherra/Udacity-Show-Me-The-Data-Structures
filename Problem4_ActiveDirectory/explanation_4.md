# Overview
I propose a recursive solution. For a given group I check whether the user matches the one present in the user list. Secondly, if the user is not there, I extract the subgroups of this group, for each subgroup I call the same function resursively, as a sub-groups might be comprised of many sub-groups themselves. The function returns `True` as soon as it


---
---
---

# Complexity
## Time complexity
Assuming that each group has maximum length of `l` users, then searching for a match within this group takes `O(l)` time. If there are `n` such groups, then each of them in the worst case scenario has to be visited. The final algorithm takes `O(n*l)` time, `n` - number of groups, `l` - length of the list holding user names (maximum observed for all groups).

## Space Complexity
Recursive calls take stack memory. The number of recursive calls depends on the longest path in the Active Directory - `m`. The amount of memory needed is also increase linearly with the number of sibling nodes `k` along the longest path. So the final space complexity is `O(m*k)`. 