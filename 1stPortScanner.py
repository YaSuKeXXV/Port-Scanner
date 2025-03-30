import socket
import threading

def scan_port (target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")

            sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

        def scan_target(target, start_port, end_port):
            print(f"\nScanning target: {target}")
            print(f"Scanning ports {start_port}{end_port}...\n")

            threads = []
            for port in range (start_port, end_port + 1):
                thread = threading.Thread(target+scan_port, args=(target,port))
                threads.append(thread)
                threads.start()

                for Thread in threads:
                    threads.join()

                    print("\nScanning complete.")

                    if __name__=="__main__":
                        target = input ("Enter target IP or domain: ")
                        start_port = int(input("Enter start port: "))
                        end_port = int(input("Enter end port: "))

                        scan_target(target, start_port, end_port)

