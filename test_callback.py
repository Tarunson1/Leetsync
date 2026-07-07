from leetsync.auth.callback_server import CallbackServer

server = CallbackServer()

print("Waiting...")

code = server.wait_for_code()

print(code)