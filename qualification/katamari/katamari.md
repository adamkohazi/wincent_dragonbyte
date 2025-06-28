# Statement
You are a large ball on an infinite horizontal plane. You start at time 0, touching the plane at the location (0,0). Your initial weight is w.

You are free to roll in any direction you like, at 1 unit of distance per second.

On the plane there are n objects, numbered from 0 to n-1. For the purpose of this task we will consider them to be points. Object i is located at coordinates (xi,yi) and has weight zi.

If you are at the same location as one of the objects and your weight is strictly greater than twice the weight of the object, you may spend 1 second to assimilate it. Doing so turns you into a bigger sphere – the weight of the assimilated object is added to your weight.

Your primary objective is to create a sphere that is as heavy as possible. Your secondary objective is to achieve the primary objective as quickly as possible.

# Special rules
Resubmissions for this problem do not generate penalty minutes.

(Note that the 20-submission limit is still in place.)

# Input format
The first line of the input file contains the number t of test cases. The specified number of test cases follows, one after another.

Each test case starts with a line containing the integers n and w. Then, n lines follow. The i-th of these lines (numbering from 0) contains the integers xi, yi, and zi.

# Output format
For each test case output two lines. The first line should contain the number k of items you want to collect, and the second line should contain a space-separated sequence of items in the order you want to collect them. (If k is zero, the second line should be present and empty.)