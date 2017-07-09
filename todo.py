#To do list
import time


def main():
	tasks = open('tasks.txt','a')
	menuSelection = menu()

	while menuSelection != 4:
		if menuSelection == 1:
			enterTask()



def menu():
	print('Menu:\n')
	print('1. Enter a task')
	print('2. Delete a task')
	print('3. View tasks')
	print('4. Exit')
	menuSelection = int(input('> '))
	return menuSelection

def enterTask():
	task = input('Enter task.\n> ')





main()

	

