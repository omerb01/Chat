import socket
import threading

clients = []

def listen_thread(conn, addr):
	print_addr = addr[0] + ":" + str(addr[1])
	while True:
		try:
			data = conn.recv(2048)
		except:
			print(print_addr + " disconnected")
			clients.remove((conn, addr))
			break
		send_all_clients(data, conn, print_addr)
		print(print_addr + ":", data.decode())
	conn.close()

def send_all_clients(data, currect_conn, print_addr):
	data = print_addr + ": " + data.decode()
	for client in clients:
		if client[0] != currect_conn:
			client[0].sendall(data.encode())

def main():

	host = "localhost"
	port = 8123

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.bind((host, port))
	except socket.error as e:
		print(str(e))

	s.listen(5)
	print("waiting for connection...")

	while True:

		conn, addr = s.accept()
		clients.append((conn, addr))
		print("connected to: " + addr[0] + ":" + str(addr[1]))
		threading.Thread(target=listen_thread, args=(conn, addr)).start()

if __name__ == "__main__":
	main()