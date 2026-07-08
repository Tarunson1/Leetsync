# from __future__ import annotations

# from http.server import BaseHTTPRequestHandler, HTTPServer
# from urllib.parse import urlparse, parse_qs


# class OAuthCallbackHandler(BaseHTTPRequestHandler):
#     authorization_code: str | None = None

#     def do_GET(self):
#         parsed = urlparse(self.path)

#         if parsed.path != "/callback":
#             self.send_error(404)
#             return

#         params = parse_qs(parsed.query)

#         OAuthCallbackHandler.authorization_code = (
#             params.get("code", [None])[0]
#         )

#         self.send_response(200)
#         self.send_header("Content-Type", "text/html")
#         self.end_headers()

#         self.wfile.write(
#             b"""
#             <html>
#                 <body>
#                     <h2>Authentication Successful</h2>
#                     <p>You may close this window.</p>
#                 </body>
#             </html>
#             """
#         )

#     def log_message(self, format, *args):
#         # Silence default HTTP logs
#         return


# class CallbackServer:

#     def __init__(
#         self,
#         host: str = "localhost",
#         port: int = 8000,
#     ):
#         self.server = HTTPServer(
#             (host, port),
#             OAuthCallbackHandler,
#         )

#     def wait_for_code(self) -> str | None:
#         self.server.handle_request()

#         return OAuthCallbackHandler.authorization_code