#To do list
import time


def main():
	menuSelection = menu()

	while menuSelection != 4:
		
		if menuSelection == 1:
			enterTask()
			menuSelection = menu()
		if menuSelection == 3: 
			viewTask()
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
	tasks = open('tasks.txt','a')
	proceed = 'y'
	
	while proceed == 'y':
		taskName = input('Enter the task name.\n> ')
		
		tasks.write(str(taskName) + '\n')

		proceed = input('Enter another task? (y/n): ')
	print('Saved tasks!\n')
	tasks.close()

def viewTask():
	tasks = open('tasks.txt','r')
	for entry in tasks:
		entry.rstrip('\n')
		print(entry)
	tasks.close()





main()

	

