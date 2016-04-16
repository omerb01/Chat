import socket
import threading

def send_thread(conn):
	print("welcome to chat, type anything: ")

	while True:
		data = input()
		try:
			conn.sendall(data.encode())
		except:
			break
	conn.close()

def listen_thread(conn):
	while True:
		try:
			data = conn.recv(2048)
		except:
			break;
		print(data.decode())

def main():

	server = "localhost"
	port = 8123

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.connect((server, port))
	except socket.error as e:
		print(str(e))

	t = threading.Thread(target=send_thread, args=(s,))
	t.daemon = True
	t.start()

	threading.Thread(target=listen_thread, args=(s,)).start()

if __name__ == "__main__":
	main()