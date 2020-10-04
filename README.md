# cf-FetchProblems

This is a simple python script which fetches problems of division 3 and division 2 based on the tags and rating provoded by the user from a competitive platform "CodeForces" and then selects the number of problems as per users's wish from that. 

This can be used to motivate the programmers who are new to competitive, by giving them questions based on their requirements everyday. Also, this script makes sure that no problems are repeated which are already solved before by the programmers.

# How to use ?

This script uses codeforces API to find the URL of problems, hence we need to install the requests.

```
pip install -r requirements.txt
```

To run the program

1. There is a file named user.txt which should contain all the user handles (of codeforces) who are going to use this script. 	

   Example, user.txt contains the following handles (of codeforces):

   nancyradadia

   yashrajkakkad

2. To run the python script:

   ```
   python fetch_problems.py
   ```

   

# Output

You will get a text message containing 3 problems follwed by URL link in the file named "message.txt" which you can share on whatsapp group and motivate all the programmers to solve the problems.
Problems are fetched from the TAG which you provide in "tags" variable. To give mutiple tags use semicolon, eg tags = 'implementations; dp'. If you keep tag empty (tag = '') then problems across all tags will be fetched.

Example: tags = '' (hence problems across all tags are fetched)

```
Today's problems: 
*Category A*: https://www.codeforces.com/problemset/problem/195/A
*Category B*: https://www.codeforces.com/problemset/problem/1061/B
*Category C*: https://www.codeforces.com/problemset/problem/165/C
If you're new to CP, solve A, B, C. Once you solve it reply with 👍 to motivate others
```

# References
This script refers code from the following open source repository:
+ [cf-educational](https://github.com/yashrajkakkad/cf-educational)

