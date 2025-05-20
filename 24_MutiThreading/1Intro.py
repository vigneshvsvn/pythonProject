"""
Multi Tasking:    executing several tasks simultaneously

Advantage:
- reduce the program execution time.
- performance is going to Increase.

1. Process-Based MultiTask: '
	executing several tasks simultaneously, where each task is a separate independent program /process at OS Level.
	Eg: Typing code in IDE, listing music, downloading new songs…

2. Thread-Based Multitasking:
	executing multiple tasks simultaneously, where each task is a separate independent part of the same program /process.
	Eg:  

Thread:
- independent part of the same program.
- is flow of execution.

Module Name: threading

	Main Tread: Evey program is one flow. That flow is called main Tread.
				current_thread().getName()
				By Default, every python program is having one flow called Main Flow with main Thread.

Ways of Creating thread.
1. Creating a thread without using any class --> Functional Programming
2. Creating a thread with extending Thread class --> Oops
3. Creating a thread without extending Thread Class

When to go for Multithreaded:
- When we have independent part of the same program. Then we need to go for Multi Thread.

"""

import threading

print('Current Executing Thread Name:',threading.current_thread().name)