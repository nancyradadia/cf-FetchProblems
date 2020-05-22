import requests
import random

# Here empty tag will fetch all problems
# it can be tags = "implementation;dp;math"
tags = ''

handles = [line.rstrip('\n') for line in open("users.txt")] # this will store all the user handles from users.txt in a list


# function to get ID of all the contest of divison 2 and division 3
def get_id():
    response = requests.get('https://codeforces.com/api/contest.list')
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]
    ids = []
    for contest in response:
        if(contest["name"].find("Div. 2")!= -1 or contest["name"].find("Div. 3")!= -1):
            ids.append(contest["id"])

    ids.sort()
    return ids


# function to get ID of all the contest which are correctly solved by the users
def get_user_handle_ids():
    ids = []
    for i in range(len(handles)):
        response = requests.get('https://codeforces.com/api/user.status', params={"handle": handles[i]})
        response.raise_for_status()
        response = response.json()
        if response["status"] != "OK":
            print("Invalid response")
            exit()
        response = response["result"]

        for problem in response:
            try:
                if(problem["verdict"]=='OK'):
                    ids.append(problem["contestId"])
            except:
                continue
    id1 = set(ids)
    return id1


# to eleminate all the solved contest ids (by user) and to get problems from the contest id's and generate url
def get_problems():

    id1 = get_id()
    id2 = get_user_handle_ids()
    ids = set(id1) - set(id2)

    response = requests.get(
        'https://codeforces.com/api/problemset.problems', params={"tags": tags})
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]
    problems_response = response["problems"]
    problemA = []
    problemB = []
    problemC = []
    problems = []

    for problem in problems_response:
        try:
            if problem["contestId"] in ids and (problem["rating"]>900 and problem["rating"]<1300):
                url = 'https://www.codeforces.com/problemset/problem/' + \
                    str(problem["contestId"]) + '/' + problem["index"]
                problemA.append( url)
            if problem["contestId"] in ids and (problem["rating"]>1200 and problem["rating"]<1500):
                url = 'https://www.codeforces.com/problemset/problem/' + \
                    str(problem["contestId"]) + '/' + problem["index"]
                problemB.append( url)
            if problem["contestId"] in ids and (problem["rating"]>1400 and problem["rating"]<1700):
                url = 'https://www.codeforces.com/problemset/problem/' + \
                    str(problem["contestId"]) + '/' + problem["index"]
                problemC.append(url)
        except:
            continue

    i = random.randint(0, len(problemA)-1)
    problems.append(problemA[i])
    i = random.randint(0, len(problemB)-1)
    problems.append(problemB[i])
    i = random.randint(0, len(problemC)-1)
    problems.append(problemC[i])

    return problems


# main function
if __name__ == "__main__":
    prob = get_problems()
    with open('message.txt', 'w', encoding='utf-8') as f:
        message = "Today's problems: \n*Category A*: "+prob[0]+"\n*Category B*: "+prob[1]+"\n*Category C*: "+prob[2]+"\nIf you're new to CP, solve A, B, C. Once you solve it reply with 👍 to motivate others"
        f.write(message)

    # print(message)
