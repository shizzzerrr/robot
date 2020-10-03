x, y = list(map(int, input().split())) #размеры поля
plain, history, result = {}, [], 0
for a in range(1, y+1):
	for b in range(1, x+1):
		plain[str(b) + str(a)] = list(map(int, input().split()))
start = input().replace('L', '0').replace('T', '1').replace('R', '2').replace('B', '3').split()
robots = [[start[0]+start[1], int(start[2]), 0]]
while robots != []:
	robot = robots[0]
	robots.remove(robot)
	if robot[0]+str(robot[1]) in history:
		continue
	history += [robot[0]+str(robot[1])]
	if (robot[0][0]=='0') or (robot[0][1]=='0') or (robot[0][0]==str(x+1)) or (robot[0][1]==str(y+1)):
		result = robot[2]
		break
	if plain[robot[0]][robot[1]] == False:
		if robot[1] == 0:
			robots += [[str(int(robot[0])-10), robot[1], robot[2]+1]]
		elif robot[1] == 1:
			robots += [[str(int(robot[0])-1), robot[1], robot[2]+1]]
		elif robot[1] == 2:
			robots += [[str(int(robot[0])+10), robot[1], robot[2]+1]]
		elif robot[1] == 3:
			robots += [[str(int(robot[0])+1), robot[1], robot[2]+1]]
	if robot[1] == 3:
		robot[1] = -1
	if plain[robot[0]][robot[1]+1] == False:
		if robot[1]+1 == 0:
			robots += [[str(int(robot[0])-10), robot[1]+1, robot[2]+1]]
		elif robot[1]+1 == 1:
			robots += [[str(int(robot[0])-1), robot[1]+1, robot[2]+1]]
		elif robot[1]+1 == 2:
			robots += [[str(int(robot[0])+10), robot[1]+1, robot[2]+1]]
		elif robot[1]+1 == 3:
			robots += [[str(int(robot[0])+1), robot[1]+1, robot[2]+1]]
print(result)