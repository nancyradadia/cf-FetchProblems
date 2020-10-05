import requests
import random

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
def get_problems(tags, minr, maxr, n):

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
    problems = []
    result = []


    for problem in problems_response:
        try:
            if problem["contestId"] in ids and (problem["rating"]>minr and problem["rating"]<maxr):
                url = 'https://www.codeforces.com/problemset/problem/' + \
                    str(problem["contestId"]) + '/' + problem["index"]
                problems.append( url)
        except:
            continue

    x = min(n, len(problems))

    while x>0:
        i = random.randint(0, len(problems)-1)
        result.append(problems[i])
        x-=1
    
    return result


# main function
if __name__ == "__main__":
    print("Enter \";\" seperated tags :", end=" ")
    tag = input()
    print("Enter minimum rating :", end=" ")
    min_rating = int(input())
    print("Enter maximum rating :", end=" ")
    max_rating = int(input())
    print("Enter maximum number of problems you want :", end=" ")
    num = int(input())
    print("Here are the problem links!")
    prob = get_problems(tag, min_rating, max_rating, num)

    for eachprob in prob:
        print(eachprob)