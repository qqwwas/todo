#To do list
import time

tasks = open('tasks.txt','a')
def main():
	menuSelection = menu()

	while menuSelection != 4:
		
		if menuSelection == 1:
			enterTask()
			menuSelection = menu()


def menu():
	print('\nMenu:')
	print('1. Enter a task')
	print('2. Delete a task')
	print('3. View tasks')
	print('4. Exit')
	menuSelection = int(input('> '))
	return menuSelection

def enterTask():
	proceed = 'y'
	
	while proceed == 'y':
		task = input('Enter task.\n> ')
		tasks.write(str(task) + '\n')

		proceed = input('Enter another task? (y/n): ')
	print('Saved tasks!\n')

def deleteTask():
	





main()

	

