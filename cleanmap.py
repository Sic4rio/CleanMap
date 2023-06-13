import re
import readline
import glob

# Enable tab completion for file paths
readline.parse_and_bind('tab: complete')

# Define color codes
RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
ENDC = "\033[0m"

# Print the banner in red color
print(RED + '''

 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███╗   ███╗ █████╗ ██████╗     
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔══██╗██╔══██╗    
██║     ██║     █████╗  ███████║██╔██╗ ██║██╔████╔██║███████║██████╔╝    
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     
╚██████╗███████╗███████╗██║  ██║██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝    
		            |	=== Ports +  URLs === | 
''' + ENDC)

try:
    # Prompt the user to enter the address to append the ports to
    address = input("Enter the address to append the ports to: ")

    # Prompt the user to enter the file location and name
    file_path = input("Enter the location and name of the file: ")

    # Perform file path completion using glob module
    matched_files = glob.glob(file_path + '*')
    if matched_files:
        file_path = matched_files[0]

    # Read the Nmap results from the text file
    with open(file_path, 'r') as file:
        nmap_results = file.read()

    # Extract the port numbers using regular expressions
    port_numbers = re.findall(r'\b(\d+)/tcp', nmap_results)

    # Generate URLs with port numbers
    urls_with_ports = [f"{address}:{port}" for port in port_numbers]

    # Prompt the user to choose the output option
    output_option = input("Enter '1' to display output in console or '2' to save it in a text file: ")

    # Perform the chosen output option
    if output_option == "1":
        # Display output in console
        # Print the generated URLs with color
        for url in urls_with_ports:
            print(BRIGHT_GREEN + url + ENDC)

    elif output_option == "2":
        # Save output in a text file
        # Prompt the user to enter the output file name
        output_file_name = input("Enter the name of the output file (without extension): ")
        output_file_path = output_file_name + ".txt"

        # Write the generated URLs to the output file
        with open(output_file_path, 'a') as output_file:
            # Write the generated URLs
            for url in urls_with_ports:
                output_file.write(url + "\n")

        print(BRIGHT_GREEN + f"Output saved in {output_file_path}" + ENDC))
    else:
        print("Invalid option. Please enter either '1' or '2' for the output option.")

except FileNotFoundError:
    print(f"File not found: {file_path}")

except KeyboardInterrupt:
    print("\nKeyboard interrupted. Exiting...")
