import subprocess

def scan_network(ip_range):
    command = f"sudo nmap -sn {ip_range}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

def parse_output(output):
    lines = output.decode().splitlines()
    results = []
    for line in lines:
        if "Nmap scan report for" in line:
            ip_address = line.split("Nmap scan report for ")[-1].split(" ")[0]
            results.append(ip_address)
    return results

def print_results(results):
    print("Connected Devices:")
    for index, ip in enumerate(results, start=1):
        print(f"{index}. {ip}")

if __name__ == "__main__":
    ip_range = "192.168.0.1/24"  # Adjust the IP range as needed
    output = scan_network(ip_range)
    devices = parse_output(output)
    print_results(devices)
    print("follow me in instagram esefkh740_")