Q.What are the components of a process?
Answer:-
Process:- 
* A process is an instance of a computer program that is being execueted.
* A bundle of elements kept by the Kernel to keep track of all these running tasks.
There are following components :-
1) Process ID:- The process ID (or the PID) is assigned by the operating system and is unique to each running process.
2) Memory :- Each process gets its own memory that others cannot access.
3) Code & data :- A process can be further divided into code and data sections. Program code and data should be kept 
   separately since they require different permissions from the operating system and separation facilitates sharing of code
4) The Stack:- Stacks are fundamental to function calls. Each time a function is called it gets a new stack frame.
5) The Heap :- The heap is an area of memory that is managed by the process for on the fly memory allocation.
   This is for variables whose memory requirements are not known at compile time.
6) File Descriptors:-
   * The kernel gives stdin, stdout and stderr to every process as default.
   * It also keeps track of other open files by assigning a number called a file descriptor.
   * File descriptors have permissions stdin, stdout and stderr have file desciptors 0,1 and 2 respectively.

7) Registers and kernel state:-
  * A CPU performs simple math operations inside the , limited,resigter, memory.
  * The OS needs to keep track of these registers as there will hundereds of 
    process running on a system at a time.
  * when it comes time for the currently running process to give up the processor 
    so another process can run, it needs to save its current state.
  * Equally, OS to be able to restore this state when the process is given more time to run on the CPU.
    To do this the OS needs to store a copy of the CPU registers to memory.
     When it is time for the process to run again, the OS will copy the register values back 
     from memory to the CPU registers and the process will be right back where it left off.
     Internally, the kernel needs to keep track of a number of elements for each process.
