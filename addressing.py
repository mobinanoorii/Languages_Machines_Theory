import re

url = dict()
params = dict()

n = int(input())

for i in range(n):
    url_name = input()
    add = input()
    url[url_name] = add

t = int(input())

for i in range(t):
    u_name = input()
    s_params = input()
    params[u_name] = s_params

for u_n, s_p in enumerate(params):

    if u_n in url.keys:
        val = url[u_n]
        p = re.split("\s", s_p)
        for x in p:
            pattern = re.split("=", x)
            final = re.sub(pattern[0], pattern[1], val)
            print(final)

    else:
        print("[Error] url not found")
