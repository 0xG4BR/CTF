import gdb

def send_input(input_str):
    # Convert the input string to bytes and write to the program's STDIN
    with open('inputs.txt','w') as f:
        f.write(input_str)
    gdb.execute('r < inputs.txt')

def continue_with_input(input_str):
    # Send input to the program and continue execution
    send_input(input_str)
 
def read_memory(address, size):
    # Read memory content at the given address and return the bytes
    inferior = gdb.selected_inferior()
    mem = inferior.read_memory(address, size)
    return mem.tobytes()

def rsp_value():
    rsp_offset = 0x70
    rsp_addr = gdb.selected_frame().read_register("rsp") + rsp_offset
    mem_value = gdb.selected_inferior().read_memory(rsp_addr, 8)  # Adjust the size (8 bytes) if needed
    value = mem_value.tobytes()
    print("bytes = ",value)
    return int.from_bytes(value,"little")



def main():
    flag = "AS"
    gdb.execute('b* 0x0000555555555bb7')  # Change this to the function where you want to break
    
    for j in range(38):
        for i in range(33,127):
            # Set breakpoints
            print(flag+chr(i))
            # Initialize breakpoint counter
            continue_with_input(flag+chr(i))
            value_at_addr = rsp_value()

            for k in range(0,len(flag+chr(i)) + 2):
                value_at_addr = rsp_value()
                print("hex",hex(value_at_addr))
                #Check if signal
                while value_at_addr > 0x555555550000 and k > 1:
                    print("here",k)
                    gdb.execute("fini")
                    value_at_addr = rsp_value()
                    print("hex",value_at_addr)


                gdb.execute("c")
                
            if value_at_addr == 0:
                flag += chr(i)
                print(f"current flag: {flag}")
                # gdb.execute('q')  # Exit GDB
                break 

if __name__ == "__main__":
    main()
