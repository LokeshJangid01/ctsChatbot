# from http.server import BaseHTTPRequestHandler, HTTPServer
# import os
# from urllib.parse import unquote

# hostName = "192.168.0.105"  # Replace with your actual IP address
# serverPort = 8080

# class MyServer(BaseHTTPRequestHandler):
#     def do_GET(self):
#         # Decode the URL path to handle spaces and other special characters
#         file_path = unquote(self.path)

#         # If no specific file is requested, serve index.html by default
#         if file_path == "/" or file_path == "":
#             file_path = "/index.html"

#         # Construct full file path
#         full_path = os.path.join(os.getcwd(), file_path.lstrip("/"))
#         # Check if the requested file exists
#         if os.path.exists(full_path):
#             # Determine the content type based on the file extension
#             if file_path.endswith(".html"):
#                 content_type = "text/html"
#             elif file_path.endswith(".css"):
#                 content_type = "text/css"
#             elif file_path.endswith(".js"):
#                 content_type = "application/javascript"
#             elif file_path.endswith(".png"):
#                 content_type = "image/png"
#             elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
#                 content_type = "image/jpeg"
#             else:
#                 content_type = "application/octet-stream"
#         # If the path is just '/', serve index.html
#         # if self.path == "/" or self.path == "/index.html":
#         #     self.send_response(200)
#         #     self.send_header("Content-type", "text/html")
#         #     self.end_headers()

#         #     # Serve index.html file
#         #     if os.path.exists("index.html"):
#         #         with open("index.html", "r") as file:
#         #             html_content = file.read()
#         #             self.wfile.write(bytes(html_content, "utf-8"))
#         #     else:
#         #         self.wfile.write(bytes("<html><body><h1>404 Not Found</h1></body></html>", "utf-8"))
#         # else:
#         #     # For any other path, return 404 Not Found
#         #     self.send_response(404)
#         #     self.send_header("Content-type", "text/html")
#         #     self.end_headers()
#         #     self.wfile.write(bytes("<html><body><h1>404 Not Found</h1></body></html>", "utf-8"))

# if __name__ == "__main__":
#     webServer = HTTPServer((hostName, serverPort), MyServer)
#     print("Server started http://%s:%s" % (hostName, serverPort))

#     try:
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     webServer.server_close()
#     print("Server stopped.")
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from urllib.parse import unquote

hostName = "192.168.0.105"  # Replace with your actual IP address
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Decode the URL path to handle spaces and special characters
        file_path = unquote(self.path)

        # If no specific file is requested, serve index.html by default
        if file_path == "/" or file_path == "":
            file_path = "/index.html"

        # Construct full file path
        full_path = os.path.join(os.getcwd(), file_path.lstrip("/"))

        # Check if the requested file exists
        if os.path.exists(full_path):
            # Determine the content type based on the file extension
            if file_path.endswith(".html"):
                content_type = "text/html"
            elif file_path.endswith(".css"):
                content_type = "text/css"
            elif file_path.endswith(".js"):
                content_type = "application/javascript"
            elif file_path.endswith(".png"):
                content_type = "image/png"
            elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                content_type = "image/jpeg"
            elif file_path.endswith(".gif"):
                content_type = "image/gif"
            elif file_path.endswith(".svg"):
                content_type = "image/svg+xml"
            else:
                content_type = "application/octet-stream"

            # Serve the file
            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()

            # Open and serve the file (binary mode for images and other non-text files)
            with open(full_path, "rb") as file:
                self.wfile.write(file.read())
        else:
            # File not found, return 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><body><h1>404 Not Found</h1></body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
